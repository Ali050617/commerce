from django.db import models
from products.base_model import BaseModel
from products.models import Product


class Cart(BaseModel):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_total(self):
        self.total_price = sum(product.price for product in self.products.all())
        self.save()

    def __str__(self):
        return self.products
 