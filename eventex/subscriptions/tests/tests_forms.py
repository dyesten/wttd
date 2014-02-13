# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeFormTest(TestCase):
	def test_has_fields(self):
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)