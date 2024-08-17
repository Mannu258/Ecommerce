from typing import Any
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cateogery(models.Model):
    cat = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.cat

class subcateogery(models.Model):
    ccat = models.ForeignKey(Cateogery,on_delete=models.CASCADE)
    scat = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.scat

class Product(models.Model):
    cat = models.ForeignKey(subcateogery,on_delete=models.CASCADE)
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images',default="")

    def __str__(self) -> str:
        return self.product_name

class ContactUs(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.EmailField()
    phone = models.IntegerField()
    messege = models.CharField(max_length=500,default='')
    def __str__(self) -> str:
        return self.name
   

    
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default = 'root')
    order_date = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    email = models.EmailField()
    address1= models.CharField(max_length=500)
    address2= models.CharField(max_length=500,default ='')
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    zip = models.IntegerField()
    payment = models.CharField(max_length=30)

    def __str__(self) -> str:
        return '%s'%self.product
    
class UserDetails(models.Model):
    Username = models.CharField(max_length = 60,blank = True, null =True)
    name = models.CharField(max_length = 30,null =True)
    email = models.EmailField(null =True)
    number = models.IntegerField(null =True)
    def __str__(self) -> str:
        return self.Username
    
    
    
