from __future__ import unicode_literals
from django.db import models
from  django.utils.timezone import now

class Config(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    value =  models.CharField(max_length = 100)

class State(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    value = models.CharField(max_length = 100)
    last_updated = models.DateTimeField(default= now)

class Note(models.Model):
    text = models.CharField(max_length=1024)