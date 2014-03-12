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
	
	#test com erro	
	def test_cpf_is_not_valid(self):
		form = self.make_validated_forms(cpf='12345678901')
		#self.assertFalse(form.errors)
		self.assertItemsEqual(['cpf'], form.errors)


	
	
	def test_email_is_optional(self):
		form = self.make_validated_forms(email="")
		self.assertFalse(form.errors)
	
	def test_name_must_be_capitalized(self):
		form = self.make_validated_forms(name='DYESTEN dE paulon')
		self.assertEqual('Dyesten de Paulon', form.cleaned_data['name'])

	def test_must_inform_email_or_phone(self):
		form = self.make_validated_forms(email='', phone_0='', phone_1='')
		self.assertItemsEqual(['__all__'], form.errors)
		
	def make_validated_forms(self, **kwargs):
		data = dict(name='Dyesten Paulon', email='dyesten.pt@gmail.com', cpf='11144477735', phone_0='31', phone_1='88994477')
		data.update(kwargs)
		form = SubscriptionForm(data)
		form.is_valid()

		return form
	