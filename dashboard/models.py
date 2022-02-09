from operator import mod
from sre_constants import CATEGORY
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY=(('Statonary','Statonary'),('Electronics','Electronics'),('Food','Food'))

class Product(models.Model):
       name=models.CharField(max_length=100,null=True)
       category=models.CharField(max_length=20,choices=CATEGORY, null=True)
       quantity=models.PositiveIntegerField(null=True)

       class Meta:
              verbose_name_plural='Product'

       def __str__(self):
              return f'{self.name}'


class Order(models.Model):
       product=models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
       staff=models.ForeignKey(User,models.CASCADE,null=True)
       order_quantity=models.PositiveIntegerField(null=True)
       date=models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return f'{self.product}-{self.order_quantity}, Ordered by {self.staff.username}'