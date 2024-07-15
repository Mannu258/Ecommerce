from typing import Any
from django.db import models

# Create your models here.

class Cateogery(models.Model):
    cat = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.cat

class Product(models.Model):
    cat = models.ForeignKey(Cateogery,on_delete=models.CASCADE)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=60)
    price = models.IntegerField()
    

    def __str__(self) -> str:
        return self.item_name
