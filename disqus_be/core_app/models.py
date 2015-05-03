"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    pub_time = models.DateTimeField(auto_now_add=timezone.now)
    is_public = models.BooleanField(default=True)
    author_title = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
