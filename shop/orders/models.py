from django.db import models
from users.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    # Це означає, що одне замовлення може містити кілька товарів, і один товар може належати до кількох замовлень.

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'id: {self.id}, user: {self.user.username}'

