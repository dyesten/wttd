# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
	def setUp(self):
		s = Subscription.objects.create(name='Dyesten Paulon', cpf='123456789012', email='dyesten.pt@gmail.com', phone='31-88996655')
		self.resp = self.client.get('/inscricao/%d/' % s.pk)
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
	
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')
		
	def test_context(self):
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)
	
	def test_html(self):
		self.assertContains(self.resp, 'Dyesten Paulon')

class DetailNotFound(TestCase):
	def test_not_found(self):
		response = self.client.get('/inscricao/0/')
		self.assertEqual(404, response.status_code)
		