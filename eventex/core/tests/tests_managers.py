# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact, Talk

class ContactManagerTest(TestCase):
	def setUp(self):
		s = Speaker.objects.create(name='Dyesten Paulon', slug='dyesten-paulon', url='http://dyestenpaulon.net')
		s.contact_set.add(Contact(kind='E', value='dyesten.pt@gmail.com'),
						Contact(kind='P', value='31-88776655'),
						Contact(kind='F', value='31-11223344'))
	
	def test_emails(self):
		qs = Contact.emails.all()
		expected = ['<Contact: dyesten.pt@gmail.com>']
		self.assertQuerysetEqual(qs, expected)
	
	def test_phones(self):
		qs = Contact.phones.all()
		expected = ['<Contact: 31-88776655>']
		self.assertQuerysetEqual(qs, expected)
	
	def test_faxes(self):
		qs = Contact.faxes.all()
		expected = ['<Contact: 31-11223344>']
		self.assertQuerysetEqual(qs, expected)

class PeriodManagerTest(TestCase):
	def setUp(self):
		Talk.objects.create(title='Morning Talk', start_time='10:00')
		Talk.objects.create(title='Afternoon Talk', start_time='12:00')
	
	def test_morning(self):
		self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title)
	
	def test_afternoon(self):
		self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title)