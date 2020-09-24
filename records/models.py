from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date
from django.urls import reverse

# Create your models here.


class Entry(models.Model):
	head = models.CharField(max_length=255)
	account = models.CharField(max_length=255)
	amount = models.IntegerField()
	reason = models.TextField(blank=True)
	date_created = models.DateField(auto_now_add = True)
	date_edited = models.DateField(auto_now= True)



	def __str__(self):
		return self.account + ' | ' + str(self.amount)

	def get_absolute_url(self):
		#return reverse('entrydetail' , args=(str(self.id)))
		return reverse('home' )