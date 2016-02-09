try:
    from django.conf.urls import *
except ImportError:
    from django.conf.urls.defaults import *

from taggit_autosuggest.views import list_tags

urlpatterns = [
    url(r'^list/$', list_tags, name='taggit_autosuggest-list'),
]
