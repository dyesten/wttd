# coding: utf-8

from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.datetime_safe import datetime
from django.utils.translation import ugettext as _

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscription_today', 'paid')
	date_hierarchy = 'created_at'
	search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
	list_filter = ['created_at']
	
	list_per_page = 20
	#list_max_show_all = 3
	
	def subscription_today(self, obj):
		return obj.created_at.date() == datetime.today().date()
	
	subscription_today.short_description = _(u'Inscrito hoje?')
	subscription_today.boolean = True
		
admin.site.register(Subscription, SubscriptionAdmin)