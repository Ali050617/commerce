from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('detail/<int:id>/', views.cart_detail, name='cart_detail'),
    path('create/<int:cart_id>/add/<int:product_id>/', views.cart_create, name='cart_create'),
    path('delete/<int:cart_id>/remove/<int:product_id>/', views.cart_remove_product, name='delete'),
]
