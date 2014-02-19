# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get(r('subscriptions:subscribe'))
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
	
	def test_html(self):
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 6)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')
	
	def test_csrf(self):
		self.assertContains(self.resp, 'csrfmiddlewaretoken')
	
	def test_has_form(self):
		form = self.resp.context['form']
		self.assertIsInstance(form, SubscriptionForm)
	
class SubscribePostTest(TestCase):
	def setUp(self):
		data = dict(name='Dyesten Paulon', cpf='12345678901',
					email='dyesten.pt@gmail.com', phone='31-88996655')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)
		
	def test_post(self):
		self.assertEqual(302, self.resp.status_code)
	
	def test_save(self):
		self.assertTrue(Subscription.objects.exists())
	
		
class SubscribeInvalidPostTest(TestCase):
	def setUp(self):
		data = dict(name='Dyesten Paulon', cpf='123456789012', email='dyesten.pt@gmail.com', phone='31-88996655')
		self.resp = self.client.post(r('subscriptions:subscribe'), data)
		
	def test_post(self):		
		self.assertEqual(200, self.resp.status_code)

	
	def test_form_errors(self):
		self.assertTrue(self.resp.context['form'].errors)
	
	def test_dont_save(self):
		self.assertFalse(Subscription.objects.exists())