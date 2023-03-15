from django.db import models

class UserLogin(models.Model):
	username=models.CharField(max_length= 100)
	email=models.EmailField(max_length=254)
	password = models.CharField(max_length = 100)
	def __unicode__(self):
		return self.email