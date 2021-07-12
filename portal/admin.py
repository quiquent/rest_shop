from django.contrib import admin
from .models import Product



class ProductAdmin(admin.ModelAdmin):
       list_display = ('product_name', 'product_detail', 'product_price')

admin.site.register(Product, ProductAdmin)
