from django.contrib import admin
from django.forms import models
from .models import Product, Order
from django.contrib.auth.models import Group
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
       list_display=('name','category','quantity',)
       list_filter=('category',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
# admin.site.unregister(Group)

admin.site.site_header="Inventory"


