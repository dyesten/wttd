# coding: latin
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk

class TalkListTest(TestCase):
	def setUp(self):
		s = Speaker.objects.create(name='Dyesten Paulon', slug='dyesten-paulon', 
								url='http://dyestenpaulon.net', description='Passionate software developer!')
		t1 = Talk.objects.create(description=u'Descricao da palestra', title=u'Titulo da palestra', start_time='10:00')
		t2 = Talk.objects.create(description=u'Descricao da palestra', title=u'Titulo da palestra', start_time='13:00')
		t1.speakers.add(s)
		t2.speakers.add(s)
		self.resp = self.client.get(r('core:talk_list'))
	
	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
		
	def test_template(self):
		self.assertTemplateUsed(self.resp, 'core/talk_list.html')
	
	def test_html(self):
		self.assertContains(self.resp, u'Titulo da palestra', 2)
		self.assertContains(self.resp, u'10:00')
		self.assertContains(self.resp, u'13:00')
		self.assertContains(self.resp, u'/palestras/1/')
		self.assertContains(self.resp, u'/palestras/2/')
		self.assertContains(self.resp, u'/palestrantes/dyesten-paulon/', 2)
		self.assertContains(self.resp, u'Passionate software developer!', 2)
		self.assertContains(self.resp, u'Dyesten Paulon', 2)
		self.assertContains(self.resp, u'Descricao da palestra', 2)
	
	def test_morning_talk_in_context(self):
		self.assertIn('morning_talks', self.resp.context)
	
	def test_afternoon_talk_in_context(self):
		self.assertIn('afternoon_talks', self.resp.context)