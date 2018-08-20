import random
import re
def genToken(size):
	pool = "abcdefghijklmnopqrstuvwxyz1234567890"
	res = ""
	for i in range(size):
		res+= pool[random.randrange(0,len(pool))]
	return res

def validEmail(email):
	emailregex = re.compile(
				r'.*'
				r'@'
				r'.*'
				r'\..*'
		,re.IGNORECASE)
	if(re.match(emailregex,email) == None):
		return False
	else:
		return True

def validURL(url):
	uriregex = re.compile(
			r'^(?:http|ftp)s?://' # http:// or https://
			r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
			r'localhost|' #localhost...
			r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
			r'(?::\d+)?' # optional port
			r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	if(re.match(uriregex, url) == None):
		return False
	else:
		return True

def validContactform(fullname,email,message):
	errors = []
	if(validURL(email) == False):
		errors.append("Invalid Email.")
	if(fullname == ""):
		errors.append("Invalid Fullname.")
	if(message == ""):
		errors.append("Invalid Message.")
	return errors

def get_client_ip(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    ip = x_forwarded_for.split(',')[0]
	else:
	    ip = request.META.get('REMOTE_ADDR')
	return ip