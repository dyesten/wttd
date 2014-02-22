# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeFormTest(TestCase):
	def test_has_fields(self):
		form = SubscriptionForm()
		self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

	def test_cpf_is_digit(self):				
		form = self.make_validated_forms(cpf='ABCD5678901')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_cpf_has_11_digits(self):				
		form = self.make_validated_forms(cpf='1234')
		self.assertItemsEqual(['cpf'], form.errors)

	def test_email_is_optional(self):
		form = self.make_validated_forms(email="")
		self.assertFalse(form.errors)

	def make_validated_forms(self, **kwargs):
		data = dict(name='Dyesten Paulon', email='dyesten.pt@gmail.com', cpf='12345678901', phone='21-96186180')
		data.update(kwargs)
		form = SubscriptionForm(data)
		form.is_valid()

		return form
		