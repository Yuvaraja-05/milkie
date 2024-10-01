from django.db import models

# Create your models here.
class Buys(models.Model):
    name=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)
    address=models.TextField()
    phone=models.BigIntegerField()
    email=models.EmailField(max_length=254)
   
    
    
class Example(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()



class Payment(models.Model):
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    amount = models.FloatField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)