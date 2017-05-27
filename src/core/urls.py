from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from .views import *
admin.autodiscover()
urlpatterns = [
    url(r'^login/$', login, name='login', kwargs=
    {'template_name': 'core/login.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs=
    {'next_page': '/'}),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
]