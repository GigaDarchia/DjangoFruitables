from django.db import models
from django.conf import settings
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'Product: {self.product_id}'

    def get_total(self):
        return self.quantity * self.product.price
