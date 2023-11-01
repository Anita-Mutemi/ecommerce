from django.db import models
# import the user model first
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     price = models.FloatField()
#     #if false we need to ship it
#     digital = models.BooleanField(default=False, null=True, blank=True)
    
#     def __str__(self):
#         return self.name
    
class Official(models.Model):
    id = models.AutoField(primary_key=True)
    
    #relationship to the other official wear table
    suits = models.OneToOneField('Suits', on_delete=models.SET_NULL, null=True, blank=True)
    pants = models.OneToOneField('Pants', on_delete=models.SET_NULL, null=True, blank=True)
    shirts = models.OneToOneField('Shirts', on_delete=models.SET_NULL, null=True, blank=True)
    shoes = models.OneToOneField('Shoes', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Official {self.id}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id  = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
class Suits(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
class Pants(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
class Shirts(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
class Shoes(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, null=False, blank=False)
    product_id = models.IntegerField(null=False, blank=False)
    gender = models.CharField(max_length=10, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)
    digital = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
class OrderItem(models.Model):
    product = models.ForeignKey(Official, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Official, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.address
