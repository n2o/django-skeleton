from django.conf.urls import url

from . import views
import django.contrib.auth.views as authviews


urlpatterns = [
    url(r'^$', authviews.login),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^login/$', authviews.login, name='login'),  # If user is not logged in, it will redirect to login page
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
]
