from django.contrib import admin

# Register your models here.

from . models import *
admin.site.register(Cateogery)
admin.site.register(subcateogery)
admin.site.register(Product)

