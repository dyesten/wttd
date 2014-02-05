# coding: utf-8
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.conf import settings
from django.shortcuts import render

def home(request):
	#context = RequestContext(request)
	#context = {'STATIC_URL':settings.STATIC_URL}
	#return render_to_response('index.html', context)
	return render(request, 'index.html')