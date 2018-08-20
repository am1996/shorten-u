from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.http import HttpResponse,Http404,JsonResponse
from .utils import genToken,validURL,validContactform,get_client_ip
from .models import Url,Visitor
# Create your views here.

class IndexView(generic.View):
	def get(self,request):
		return render(request,"index.html",{})
	def post(self,request):
		try:
			url = request.POST.get("url")

			if(validURL(url) == False):
				return JsonResponse({"token":"No Valid Url Provided"})

			urlObj = Url.objects.get(url=url)
			return JsonResponse({
				"token": urlObj.shortUrl,
				"controlUrl": urlObj.controlUrl
				})
		except:
			url = request.POST.get("url")
			if(url == None):
				raise Http404("Url Field Not Found..")
			else:
				token = genToken(7)
				shortUrl = str(request.build_absolute_uri()) + token
				controlUrl = str(request.build_absolute_uri()) + token + ":" + genToken(7)
				urlObj = Url(url=url,shortUrl=shortUrl,controlUrl=controlUrl)
				urlObj.save()

				return JsonResponse({"token": shortUrl,"controlUrl":controlUrl})

class RedirectToView(generic.base.RedirectView):
	def get_redirect_url(self,*args, **kwargs):
		shortUrl = str(self.request.build_absolute_uri())
		url = get_object_or_404(Url,shortUrl=shortUrl)
		url.noOfVisitors+=1
		visitor = Visitor(owner=url,ip=get_client_ip(self.request))
		visitor.save()
		url.save()
		return url.url

class ContactUsView(generic.View):
	def get(self,request):
		return render(request,"contactus.html",{})
	def post(self,request):
		fullname = request.POST.get("fullname")
		email  = request.POST.get("email")
		msg = request.POST.get("message")
		errors = validContactform(fullname,email,msg)
		if(errors):
			return render(request,"contactus.html",{
				"errors":errors
				})
		return redirect("/contactus")

class ControlView(generic.list.ListView):
	template_name = "control.html"
	context_object_name = "object"
	def get_queryset(self):
		controlUrl = str(self.request.build_absolute_uri())
		owner = get_object_or_404(Url,controlUrl=controlUrl)
		queryset = Visitor.objects.filter(owner=owner)
		return queryset
