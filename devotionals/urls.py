# coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^show/(?P<year>\d)/(?P<month>\d)/(?P<day>\d)/',
        'devotionals.views.show_devotional',
        name='show_devotional'),
)