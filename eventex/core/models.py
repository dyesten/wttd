# coding: latin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager


class Speaker(models.Model):
	name = models.CharField(_('Nome'), max_length=255)
	slug = models.SlugField(_('Slug'))
	url = models.URLField(_('Url'))
	description =  models.TextField(_(u'Descri��o'), blank=True)
	
	def __unicode__(self):
		return self.name
	
	@models.permalink
	def get_absolute_url(self):
		return ('core:speaker_detail', (), {'slug': self.slug})
	
class Contact(models.Model):
	KINDS = (
		('P', _('Telefone')),
		('E', _('Email')),
		('F', _('Fax')),
			)
	speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
	kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
	value = models.CharField(_('valor'), max_length=255)
	
	objects = models.Manager()
	emails = KindContactManager('E')
	phones = KindContactManager('P')
	faxes = KindContactManager('F')
	
	def __unicode__(self):
		return self.value

class Talk(models.Model):
	title = models.CharField(_(u'T�tulo'), max_length=200)
	description = models.TextField(_(u'Descri��o'))
	start_time = models.TimeField(_(u'Hor�rio'), blank=True)
	speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrantes'))
	
	objects = PeriodManager()
	
	class Meta:
		verbose_name = _('palestra')
		verbose_name_plural = _('palestras')
		
	def __unicode__(self):
		return self.title	
	
	
	def get_absolute_url(self):
		return '/palestras/%d/' % self.pk
	
class Course(Talk):
	slots = models.IntegerField(_('vagas'))
	notes = models.TextField(_(u'observa��es'))
	
	objects = PeriodManager()