# coding: utf-8
from django.conf.urls import patterns, include, url
from eventex.subscriptions.views import SubscriptionDetail, SubscritionCreate

urlpatterns = patterns('eventex.subscriptions.views',
	url(r'^$', SubscritionCreate.as_view(), name='subscribe'),	
	url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
)
