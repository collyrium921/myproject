from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    # for rendering HTML files
    return render(request, 'index.html')