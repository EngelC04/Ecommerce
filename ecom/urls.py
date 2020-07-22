from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name = "store"),
    path('cart/',views.cart, name = "cart"),
    path('checkout/',views.checkout, name = "checkout"),
    path('main/',views.main, name = "main"),
    path('update_item/',views.updateItem, name = "checkout"),
]
