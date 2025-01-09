from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.product_create, name='product_create'),
    path('delete/<slug:slug>/', views.product_delete, name='product_delete'),
]