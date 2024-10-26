from django.db import models
from versatileimagefield.fields import VersatileImageField
from mptt.models import MPTTModel, TreeForeignKey

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    img = VersatileImageField('Image',upload_to='products', null=True, blank=True)
    short_desc = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
