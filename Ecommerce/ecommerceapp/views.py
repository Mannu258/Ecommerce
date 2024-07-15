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
    # return HttpResponse(f"{cat}")
