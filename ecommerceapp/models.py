from typing import Any
from django.db import models

# Create your models here.

class Cateogery(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.cat

class Product(models.Model):
    cat = models.ForeignKey(Cateogery,on_delete=models.CASCADE)
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images',default="")

    def __str__(self) -> str:
        return self.product_name
