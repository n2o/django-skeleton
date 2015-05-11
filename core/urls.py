from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('login.urls', namespace='login')),
]
