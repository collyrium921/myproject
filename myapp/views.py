from pyexpat import features
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
    # words = request.POST['words']
    # length = len(words.split())
    # return render(request, 'counter.html', {'length':length})

    posts =[1,2,3,4,5,'tim','tom','john']
    return render(request, 'counter.html', {'posts':posts})


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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if(password == confirmPassword):
            if(User.objects.filter(username=username).exists()):
                messages.info(request, 'Username already exists')
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username, email, password)
                user.is_active = True
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if(user is not None):
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def post(request, pk):
    return render(request, 'post.html', {'pk':pk})