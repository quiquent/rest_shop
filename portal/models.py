from django.db import models



class Product(models.Model):
       product_name = models.TextField(null=True)
       product_detail = models.TextField()
       product_price = models.CharField(max_length=4000)