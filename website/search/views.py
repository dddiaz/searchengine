from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	#return render(request,'search/index.html',{})
	#return HttpResponse('Test')
	template = loader.get_template('search/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))
