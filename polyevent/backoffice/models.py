from __future__ import unicode_literals

from django.db import models
from location_field.models.plain import PlainLocationField

# For location, a plugin might be found to select places with adress instead of GPS

class Event(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(User)
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    website = models.URLField()
    creation_datetime = models.DateTimeField()
    last_update = models.DateTimeField()
    isCancelled = models.BooleanField(default = false)

class Activity(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(User)
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    website = models.URLField()
    creation_datetime = models.DateTimeField()
    last_update = models.DateTimeField()
    isCancelled = models.BooleanField(default = false)
