from pyexpat import features
from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature1
from .models import Feature
# Create your views here.
def index1(request):
    # return HttpResponse('<h1>Hey, Welcome</h1>')
    # for rendering HTML files
    context={
        'name':'Patrick',
        'age':23,
        'nationality':'British'
    }
    # return render(request, 'index1.html',context) 
    return render(request, 'staticcss.html',context) 
    

def counter(request):
    words = request.POST['words']
    length = len(words.split())
    return render(request, 'counter.html', {'length':length})

def index(request):
    # before creating database
    # feature1 = Feature1()
    # feature1.id =0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'
    # feature1.is_true = True
    
    # feature2 = Feature1()
    # feature2.id =0
    # feature2.name = 'Reliable'
    # feature2.details = 'Our service is very reliable'
    # feature2.is_true = False

    # feature3 = Feature1()
    # feature3.id =0
    # feature3.name = 'Easy to use'
    # feature3.details = 'Our service is very easy'
    # feature3.is_true = True

    # features=[feature1, feature2, feature3]

    features = Feature.objects.all()
    return render(request, 'index.html', {'features':features})   