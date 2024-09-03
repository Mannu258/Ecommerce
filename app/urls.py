from .views import *
from django.urls import path
urlpatterns = (
    [
        path("", index, name="home"),
        path("about", about, name="about"),
        path("cart", cart, name="cart"),
        path("contact", contact, name="contact"),
        path("login", custom_login, name="login"),
        path("custom_logout", custom_logout, name="logout"),
        path("search/<str:param>", search, name="search"),
        path("product", product, name="product"),
        path("register", register, name="register"),
        path("detail/<int:id>", detail, name="detail"),
        path("Cateogery/<str:cat>", cateogery, name="cat"),
        path("subcaterogery/<str:cat>", SUBcateogery, name="subcat"),
    ]
)
