from django.db import models
from products.base_model import BaseModel
from products.models import Product


class Checkout(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    card_number = models.CharField(max_length=20, unique=True)
    date = models.CharField(max_length=5)
    cvv = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='products')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.city}"
