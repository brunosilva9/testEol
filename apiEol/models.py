from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Context(models.Model):
    """
        Model
        # [   'user_id', 'path', 'course_id', 'org_id','course_user_tags X','asides X', 'module']
        Course Tag and Asides always empty        
    """
    #def __str__(self):
    #    return self.course_id

    user_id = models.IntegerField(default=0, null=True)
    path = models.CharField(max_length=255, default='', null=True)
    course_id = models.CharField(max_length=255, default='', null=True)
    org_id = models.CharField(max_length=255, default='', null=True)
    module = models.CharField(max_length=255, default='', null=True)


class Event(models.Model):
    """
        Model 
        # ['context', 'username', 'session', 'agent', 'host', 'referer', 'accept_language', 'event', 'time', 'event_type', 'event_source', 'page'] 
        # format time 2023-04-02T23:55:05.014262+00:00 %Y-%m-%dT%H:%M:%S.%f%Z
    """
    context = models.ForeignKey(
        Context,
        on_delete=models.CASCADE,
        related_name="context")
    username = models.CharField(max_length=255, default='',null=True )
    agent = models.CharField(max_length=255, default='',null=True )
    host = models.CharField(max_length=255, default='',null=True )
    referer = models.CharField(max_length=255, default='',null=True )
    accept_language = models.CharField(max_length=255, default='',null=True )
    session = models.CharField(max_length=255, default='',null=True )
    event = models.CharField(max_length=255, default='',null=True )
    event_type = models.CharField(max_length=255, default='',null=True )
    event_source = models.CharField(max_length=255, default='',null=True )
    page = models.CharField(max_length=255, default='', null=True)
    time = models.DateTimeField(null=True, default=None, blank=True)
