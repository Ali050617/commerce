from django.db import models
from products.base_model import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name
