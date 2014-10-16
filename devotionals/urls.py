# coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^show/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/',
        'devotionals.views.show_devotional',
        name='show_devotional'),
)