"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5


# Mr.German I tried many times to use some libraries for Google authorization
# And nothing works. Some libraries doesn't work with Django 1.7 or another
# strange error
# And now I'll realize own registration.

class myUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)

    def __unicode__(self):
    	return unicode(self.name)+" "+unicode(self.email)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    pub_time = models.DateTimeField(auto_now_add=timezone.now)
    is_public = models.BooleanField(default=True)
    author_title = models.CharField(max_length=1000)
    site_url = models.CharField(max_length=150)
    image = models.CharField(max_length=1000)

    def __unicode__(self):
    	return unicode(self.author_title)+" "+unicode(self.text)
