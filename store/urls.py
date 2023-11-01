from django.urls import path
from . import views

urlpatterns = [
    # leave as empty string for base urls
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
