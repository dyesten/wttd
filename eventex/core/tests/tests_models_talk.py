# coding: latin
from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
	def setUp(self):
		self.talk = Talk.objects.create(title=u'Introdu��o ao Django', description=u'Descri��o da palestra.', start_time='10:00')
	
	def test_create(self):
		self.assertEqual(1, self.talk.pk)
	
	def test_unicode(self):
		self.assertEqual(u'Introdu��o ao Django', unicode(self.talk))
	
	def test_speakers(self):
		self.talk.speakers.create(name='Dyesten Paulon', slug='dyesten-paulon', url='http://dyestenpaulon.net')
		self.assertEqual(1, self.talk.speakers.count())
	
	def test_period_manager(self):
		self.assertIsInstance(Talk.objects, PeriodManager)