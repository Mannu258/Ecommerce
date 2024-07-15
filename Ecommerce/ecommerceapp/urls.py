from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name="home"),
    path('about',about,name='about'),
    path('cart',cart,name='cart'),
    path('contact',contact,name='contact'),
    path('login',login,name='login'),
    path('product',product,name='product'),
    path('signup',signup,name='signup'),
    path('detail',detail,name='detail'),
    path("<str:cat>",cateogery,name='cat'),
]
