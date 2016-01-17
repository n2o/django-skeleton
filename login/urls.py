from django.conf.urls import patterns, url
from login.views import *


urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),  # If user is not logged in, it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
)
