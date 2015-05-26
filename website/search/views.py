from django.shortcuts import render
from django.http import HttpResponse
from search.pickleindex import *

# Create your views here.
def index(request):
    return render (request,'search/index.html')

#Based on this example
#http://www.djangobook.com/en/2.0/chapter07.html
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
        message += " TermID: " + term_id_from_term(request.GET['q']) #ingrain
    else:
        message = 'You submitted an empty search.'
    return HttpResponse(message)

# from mysite.books.models import Book
#
# def search(request):
#     if 'q' in request.GET and request.GET['q']:
#         q = request.GET['q']
#         books = Book.objects.filter(title__icontains=q)
#         return render(request, 'search_results.html',
#             {'books': books, 'query': q})
#     else:
#         return HttpResponse('Please submit a search term.')