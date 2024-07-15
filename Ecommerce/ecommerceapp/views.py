from django.shortcuts import render
from . models import *

# Create your views here.

def index(request,cat=None):
    query = Product.objects.all()
    catquery = Cateogery.objects.all()
    return render(request,"index.html",{"query":query,"cat":catquery})
    # return HttpResponse(f"{cat}")

def cateogery(request,cat=None):
    if cat:
        query = Product.objects.filter(cat__cat__contains=cat)
    else:
        query = Product.objects.all()
    return render(request,"index.html",{"query":query})

def about(request):
    return render(request,"about.html")

def cart(request):
    return render(request,"cart.html")

def contact(request):
    return render(request,"contact.html")

def detail(request):
    return render(request,"detail.html")

def login(request):
    return render(request,"login.html")

def product(request):
    return render(request,"prodcut.html")
def signup(request):
    return render(request,"signup.html")

