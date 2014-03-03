# coding: utf-8
#from django.shortcuts import render_to_response
#from django.template import RequestContext
#from django.conf import settings
#from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from eventex.core.models import Speaker

def home(request):
	#context = RequestContext(request)
	#context = {'STATIC_URL':settings.STATIC_URL}
	#return render_to_response('index.html', context)
	return render(request, 'index.html')

def speaker_detail(request, slug):
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker': speaker}
	return render(request, 'core/speaker_detail.html', context)