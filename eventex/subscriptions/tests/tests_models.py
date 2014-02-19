# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Dyesten Paulon', 
			cpf='01234567821',
			email='dyesten.pt@gmail.com',
			phone='31-88888888'
		)
	
	def test_create(self):
		self.obj.save()
		self.assertEqual(1, self.obj.pk)
	
	def test_has_created_at(self):
		self.obj.save()
		self.assertIsInstance(self.obj.created_at, datetime)
	
	def test_unicode(self):
		self.assertEqual(u'Dyesten Paulon',  unicode(self.obj))
	
	def test_paid_default_value_is_False(self):
		self.assertEqual(False, self.obj.paid)
		
class SubscriptionUniqueTest(TestCase):
	def setUp(self):
		Subscription.objects.create(name="Dyesten Paulon", cpf='12345678901',
									email="dyesten.pt@gmail.com", phone="31-88556644")
	
	def test_cpf_unique(self):
		s = Subscription(name="Dyesten Paulon", cpf='12345678901',
						email="dyesten.outro@gmail.com", phone="31-88556644")
		self.assertRaises(IntegrityError, s.save)
	
	def test_email_unique(self):
		s = Subscription(name="Dyesten Paulon", cpf='12345678902',
						email="dyesten.pt@gmail.com", phone="31-88556644")
		self.assertRaises(IntegrityError, s.save)
		