from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    # customer_id = models.IntegerField()   
    
class Order(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # order_id = models.IntegerField()
    order_date = models.DateTimeField('order date')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Crepe(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    # crepe_id = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    crepe = models.ForeignKey(Crepe, on_delete=models.CASCADE)

class Wrap(Item):
    limit = models.IntegerField()
    group = models.CharField(max_length=200)
    pass

class Topping(Item):
    limit = models.IntegerField()
    group = models.CharField(max_length=200)
    pass

class Fruit(Item):
    limit = models.IntegerField()
    group = models.CharField(max_length=200)
    pass

class Nut(Item):
    limit = models.IntegerField()
    group = models.CharField(max_length=200)
    pass

class Beverage(models.Model):
    limit = models.IntegerField(default=1)
    group = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Side(models.Model):
    limit = models.IntegerField()
    group = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)





