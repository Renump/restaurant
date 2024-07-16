from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Restaurant(AbstractUser):
   adress = models.CharField(max_length=200,null=True)

class Food(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    prize = models.FloatField()


class Customer(models.Model):
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Reviews(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)






