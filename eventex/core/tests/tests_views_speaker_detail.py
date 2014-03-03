# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
	def setUp(self):
		Speaker.objects.create(name='Dyesten Paulon', slug='dyesten-paulon', 
								url='http://dyestenpaulon.net', description='Passionate software developer!')
								
		url = r('core:speaker_detail', kwargs={'slug':'dyesten-paulon'})
		self.resp = self.client.get(url)

	def test_get(self):
		self.assertEquals(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

	def test_html(self):
		self.assertContains(self.resp, 'Dyesten Paulon')
		self.assertContains(self.resp, 'Passionate software developer!')
		self.assertContains(self.resp, 'http://dyestenpaulon.net')

	def test_context(self):
		speaker = self.resp.context['speaker']
		self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
	def test_not_found(self):
		url = r('core:speaker_detail', kwargs={'slug':'john-doe'})
		response = self.client.get(url)
		self.assertEqual(404, response.status_code)