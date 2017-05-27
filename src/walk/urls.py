from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

from .views import *

admin.autodiscover()
urlpatterns = [
    url(r'^(?P<pk>\d+)/', WalkView.as_view(), name = 'walk_detail'),
    #url(r'^search/$', search, name = 'search'),
    url(r'^/comment/(?P<walk_id>\d+)/$', login_required(add_comment), name= 'add_comment'),
    url(r'^/like/(?P<walk_id>\d+)/$', login_required(add_like), name= 'add_like'),
    url(r'^del_comment/(?P<walk_id>\d+)/(?P<comment_id>\d+)/$', login_required(delete_comment), name= 'delete_comment'),
    url(r'^(?P<type_of_move>\w+)/$', filter, name = 'walks_filter'),
    url(r'^$', WalkList.as_view(), name = 'walks'),
]