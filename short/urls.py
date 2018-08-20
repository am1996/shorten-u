from django.conf.urls import url,include
from django.views.generic import TemplateView
from . import views

app_name = "short"
urlpatterns = [
	url(r'^$',views.IndexView.as_view()),
	url(r'^about$',TemplateView.as_view(template_name="about.html")
		,name="about"),
	url(r'^contactus$',views.ContactUsView.as_view(),name="contactus"),
	url(r'^(?P<token>.{7})$',views.RedirectToView.as_view(),name="redirectTo"),
	url(r'^(?P<token>.{7}):(?P<control>.{7})$',views.ControlView.as_view()),
]
