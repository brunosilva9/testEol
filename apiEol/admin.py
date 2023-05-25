from django.contrib import admin
from .models import Event, Context
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ('context',)
    list_display = ('context', 'username', 'session', 'agent', 'host', 'referer',
                    'accept_language', 'event', 'time', 'event_type', 'event_source', 'page')
    list_filter = ('context', 'username', 'session', 'agent', 'host', 'referer',
                   'accept_language', 'event', 'time', 'event_type', 'event_source', 'page')
    search_fields = ('context', 'username', 'session', 'agent', 'host', 'referer',
                     'accept_language', 'event', 'time', 'event_type', 'event_source', 'page')


class ContextAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'path', 'course_id', 'org_id', 'module')
    list_filter = ('user_id', 'path', 'course_id', 'org_id', 'module')
    search_fields = ('user_id', 'path', 'course_id', 'org_id', 'module')


admin.site.register(Event,EventAdmin )
admin.site.register(Context,ContextAdmin)

