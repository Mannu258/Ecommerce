from django.shortcuts import render
from . models import *

# Create your views here.

def index(request,cat=None):
    subcatquery = subcateogery.objects.all()[:8]
    query = Product.objects.all()
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
    subcatquery = subcateogery.objects.all()[:8]

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

def detail(request):
    return render(request,"detail.html")

def login(request):
    return render(request,"login.html")

def product(request):
    return render(request,"prodcut.html")
def signup(request):
    return render(request,"signup.html")

