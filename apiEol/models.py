from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Context(models.Model):
    """
        Model
        [   'user_id', 'path', 'course_id', 'org_id','course_user_tags X','asides X', 'module']
        Course Tag and Asides always empty
    """

    user_id = models.IntegerField(default=0)
    path = models.CharField(max_length=255, default='')
    course_id = models.CharField(max_length=255, default='')
    org_id = models.CharField(max_length=255, default='')
    module = models.CharField(max_length=255, default='')


class Event(models.Model):
    """
        Model 
        ['context', 'username', 'session', 'agent', 'host', 'referer', 'accept_language', 'event', 'time', 'event_type', 'event_source', 'page'] 
        # format time 2023-04-02T23:55:05.014262+00:00
    """
    context = models.ForeignKey(
        Context,
        on_delete=models.CASCADE,
        related_name="context")
    username = models.CharField(max_length=255, default='')
    agent = models.CharField(max_length=255, default='')
    host = models.CharField(max_length=255, default='')
    referer = models.CharField(max_length=255, default='')
    accept_language = models.CharField(max_length=255, default='')
    session = models.CharField(max_length=255, default='')
    event = models.CharField(max_length=255, default='')
    event_type = models.CharField(max_length=255, default='')
    event_source = models.CharField(max_length=255, default='')
    page = models.CharField(max_length=255, default='')
    time = models.DateTimeField(null=True, default=None, blank=True)




