from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))

    def __str__(self):
        return f'{self.user.username}\'s cart'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('Cart'))
    product = models.ForeignKey('shop.Product', on_delete=models.CASCADE, verbose_name=_('Product'))
    quantity = models.IntegerField(default=0, verbose_name=_('Quantity'))

    def __str__(self):
        return f'Product: {self.product_id}'

    def get_total(self):
        return self.quantity * self.product.price
