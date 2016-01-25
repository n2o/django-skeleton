from django.conf.urls import url
from login.views import *

import django.contrib.auth.views as authviews


urlpatterns = [
    url(r'^$', authviews.login),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^login/$', authviews.login, name='login'),  # If user is not logged in, it will redirect to login page
    url(r'^register/$', register, name='register'),
    url(r'^register/success/$', register_success, name='register_success'),
]
