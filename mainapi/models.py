from django.db import models

# Create your models here.

class Product(models.Model):
    date_created = models.DateField(auto_now_add=True)
    product_name = models.CharField(max_length=150)
    product_price = models.CharField(max_length=15)
    product_stock = models.CharField(max_length=10)
    
class Sales(models.Model):
    date_created = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

