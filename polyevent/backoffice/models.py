from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from location_field.models.plain import PlainLocationField

# For location, a plugin might be found to select places with adress instead of GPS

class Event(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_begin = models.DateField()
    date_end = models.DateField()
    website = models.URLField()
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField()
    isCancelled = models.BooleanField(default=False)
    isVisible = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("view_hidden_event", "Can see a hidden event"),
        )

class Activity(models.Model):
    event = models.ForeignKey(Event)
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_begin = models.DateTimeField()
    date_end = models.DateTimeField()
    website = models.URLField()
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField()
    isCancelled = models.BooleanField(default=False)
    isVisible = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        permissions = (
            ("view_hidden_activity", "Can see a hidden Activity"),
        )
