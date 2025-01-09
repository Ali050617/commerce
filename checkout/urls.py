from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.checkout_list, name='checkout_list'),
    path('detail/<int:id>/', views.checkout_detail, name='checkout_detail'),
    path('create/', views.checkout_create, name='checkout_create'),
]
