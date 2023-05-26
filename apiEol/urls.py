"""
URL configuration for backEol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .views import count_events_per_minute,  get_event_count, get_filtered_events,get_first_10_Events

urlpatterns = [
    path('get_filtered_events/', get_filtered_events, name='get_filtered_events'),
    path('get_event_count/', get_event_count, name='get_event_count'),
    path('get_first_10_Events/', get_first_10_Events, name='get_first_10_Events'),
    path('count_events_per_minute/', count_events_per_minute, name='count_events_per_minute'),




]
