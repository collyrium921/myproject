from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    # for rendering HTML files
    context={
        'name':'Patrick',
        'age':23,
        'nationality':'British'
    }
    return render(request, 'index.html', {'name':context}  