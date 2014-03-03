# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError

class SpeakerModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker(name='Dyesten Paulon', slug='dyesten-paulon', 
								url='http://dyestenpaulon.net', description='Passionate software developer!')
		self.speaker.save()
	
	def test_create(self):
		self.assertEquals(1, self.speaker.pk)		
	
	def test_unicode(self):
		self.assertEqual(u'Dyesten Paulon', unicode(self.speaker))

class ContactModelTest(TestCase):
	def setUp(self):
		self.speaker = Speaker.objects.create(name='Dyesten Paulon', slug='dyesten-paulon', 
							url='http://dyestenpaulon.net', description='Passionate software developer!')
	def test_email(self):
		contact = Contact.objects.create(speaker=self.speaker, kind = 'E', value='dyesten.pt@gmail.com')
		self.assertEqual(1, contact.pk)
	
	def test_phone(self):
		contact = Contact.objects.create(speaker=self.speaker, kind = 'P', value='31-99887766')
		self.assertEqual(1, contact.pk)
		
	def test_fax(self):
		contact = Contact.objects.create(speaker=self.speaker, kind = 'F', value='31-22114455')
		self.assertEqual(1, contact.pk)
	
	def test_kind(self):
		contact = Contact(speaker=self.speaker, kind='A', value='B')
		self.assertRaises(ValidationError, contact.full_clean)
	
	def test_unicode(self):
		contact = Contact(speaker=self.speaker, kind='E', value='dyesten.pt@gmail.com')
		self.assertEqual(u'dyesten.pt@gmail.com', unicode(contact))