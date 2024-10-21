from django.db import models
from django.conf import settings

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products', null=True, blank=True)
    short_desc = models.TextField()
    description = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name

class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.user.username