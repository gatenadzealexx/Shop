from django.db import models
from users.models import User
from catalog.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('user', 'id_product')



