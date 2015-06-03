from django.shortcuts import render
from django.http import HttpResponse
from search.pickleindex import *
from django.template import Context, Template

# Create your views here.
def index(request):
    return render (request,'search/index.html')

#Based on this example
#http://www.djangobook.com/en/2.0/chapter07.html
def search(request):
    if 'q' in request.GET:
        search_phrase = request.GET['q']
        #results = return_query_results(search_phrase);
        sr = SearchResults()
        results = sr.calcResults(search_phrase)
        context = {'results':results}
        return render(request,'search/results.html', context)
    else:
        message = 'You submitted an empty search.'
        return HttpResponse(message)

