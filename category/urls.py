from django.urls import path
from . import views


app_name = 'category'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),
    path('create/', views.category_create, name='category_create'),
]
