from .views import *
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

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
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
] +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
