from django.contrib import admin

# Register your models here to make it accessible to the admin interface

from .models import *

admin.site.register(Customer)
admin.site.register(Official)
admin.site.register(Order)
admin.site.register(Suits)
admin.site.register(Pants)
admin.site.register(Shirts)
admin.site.register(Shoes)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)