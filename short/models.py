from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Visitor(models.Model):
	owner = models.ForeignKey("Url",on_delete = models.CASCADE)
	ip = models.CharField(max_length = 30)
	date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.ip

class Url(models.Model):
	url = models.URLField(blank = False,null = False)
	controlUrl = models.URLField(blank = False,default = None)
	shortUrl = models.URLField(blank = False,null = False)
	date = models.DateTimeField(auto_now_add = True)
	noOfVisitors = models.IntegerField(default = 0)
	def __str__(self):
		return self.url