# -*- coding: latin-1 -*-

from nameparser import HumanName

from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

from eventex.subscriptions.models import Subscription

def validar_cpf(cpf):
    digitos = [int(c) for c in cpf if c.isdigit()]
    if len(digitos) == 11:
        a,b,c,d,e,f,g,h,i,j,k = digitos
        numeros = [a,b,c,d,e,f,g,h,i]
        r = range(10, 1, -1)
        soma = sum([x * y for x, y in zip(numeros, r)])
        resto = soma % 11
        dv1 = (11 - resto if 11 - resto < 10 else 0)
        numeros = [a,b,c,d,e,f,g,h,i,dv1]
        r = range(11, 1, -1)
        soma = sum([x*y for x, y in zip(numeros, r)])
        resto = soma % 11
        dv2 = (11 - resto if 11 - resto < 10 else 0)
        return dv1 == j and dv2 == k
    return False

def CPFValidator(value):	
	if not value.isdigit():
		raise ValidationError(_(u'CPF deve conter apenas números.'))
	if len(value)!=11:
		raise ValidationError(_(u'CPF deve ter 11 números.'))
	if not validar_cpf(value):
		raise ValidationError(_(u'CPF inválido.'))

class PhoneWidget(forms.MultiWidget):		
	def __init__(self, attrs=None):
		widgets = (
			forms.TextInput(attrs=attrs),
			forms.TextInput(attrs=attrs))
		super(PhoneWidget, self).__init__(widgets, attrs)
		
	def decompress(self, value):
		if not value:
			return [None, None]
		return value.split('-')

class PhoneField(forms.MultiValueField):
	widget = PhoneWidget
	
	def __init__(self, *args, **kwargs):
		fields = (forms.IntegerField(), forms.IntegerField())
		super(PhoneField, self).__init__(fields, *args, **kwargs)
	
	def compress(self, data_list):
		if not data_list:
			return ''
		if data_list[0] in EMPTY_VALUES:
			raise forms.ValidationError(_(u'DDD inválido'))
		if data_list[1] in EMPTY_VALUES:
			raise forms.ValidationError(_(u'Número inválido'))
		return '%s-%s' % tuple(data_list)
		
class SubscriptionForm(forms.ModelForm):
	phone = PhoneField(label=_('Telefone'), required=False)
	class Meta:
		model = Subscription
		exclude = ('paid',)
	
	def __init__(self, *args, **kwargs):
		super(SubscriptionForm, self).__init__(*args, **kwargs)
		self.fields['cpf'].validators.append(CPFValidator)
	
	def clean_name(self):
		name = self.cleaned_data['name'].lower()
		name = HumanName(name)
		name.capitalize()
		return unicode(name)
		#words = map(lambda w: w.capitalize(), name.split())		
		#capitalized_name = ' '.join(words)
		#return capitalized_name
	
	def clean(self):
		super(SubscriptionForm, self).clean()
		
		if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
			raise ValidationError(_(u'Informe seu e-mail ou telefone'))
		return self.cleaned_data
