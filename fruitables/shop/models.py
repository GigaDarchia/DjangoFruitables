from django.db import models
from versatileimagefield.fields import VersatileImageField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Category'))
    slug = models.SlugField(max_length=200, verbose_name=_('Slug'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    stock = models.IntegerField(default=0, verbose_name=_('Stock'))
    img = VersatileImageField(verbose_name=_('Image'),upload_to='products', null=True, blank=True)
    short_desc = models.TextField(blank=True, null=True, verbose_name=_('Short Description'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Description'))
    rating = models.PositiveIntegerField(default=0, verbose_name=_('rating'))

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(MPTTModel):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name=_('Parent'))
    slug = models.SlugField(max_length=200, verbose_name=_('Slug'))

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name
