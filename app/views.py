from django.shortcuts import render
from . models import *

# Create your views here.

def index(request,cat=None):
    subcatquery = subcateogery.objects.all()[:10]
    query = Product.objects.all()[:20]
    catquery = Cateogery.objects.all()
    return render(request,"index.html",{"query":query,"catquery":catquery,"subcatquery":subcatquery})

def cateogery(request, cat=None):
    catquery = Cateogery.objects.all()
    query = Product.objects.all()
    if cat:
        subcatquery = subcateogery.objects.filter(ccat__cat__contains=cat)
    else:
        catquery = Cateogery.objects.all()
    return render(request, "index.html", {"query":query,"catquery": catquery,"subcatquery":subcatquery})

def search(request, param):
    search_value = param
    if search_value:
        query = Product.objects.filter(product_name__icontains=search_value)
    else:
        query = Product.objects.all()
    catquery = Cateogery.objects.all()
    subcatquery = subcateogery.objects.all()

    return render(request, "index.html", {"query": query, "catquery": catquery, "subcatquery": subcatquery})
        
    

def SUBcateogery(request, cat=None):
    query = Product.objects.filter(cat__scat__contains=cat)
    catquery = Cateogery.objects.all()
    subcatquery = subcateogery.objects.all()[:8]
    
    return render(request, "index.html", {"query":query,"catquery": catquery,"subcatquery":subcatquery})


def about(request):
    return render(request,"about.html")

def cart(request):
    return render(request,"cart.html")

def contact(request):
    return render(request,"contact.html")

def detail(request,id):
    from django.http import HttpResponse
    return HttpResponse(f"{id}")
    return render(request,"detail.html")

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid credentials. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def custom_logout(request):
    from django.contrib.auth import logout
    from django.shortcuts import redirect
    logout(request)
    return redirect('/')
    
def product(request):
    return render(request,"prodcut.html")

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("Email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        return redirect('login')
    return render(request, 'registration.html')

