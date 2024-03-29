from categories.models import Category
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
import os

def product_dir_path(instance, filename):
    return os.path.join('photos/', instance.category.name, filename)

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().order_by('category', 'name', 'number')

class Product(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    display_img = models.CharField(max_length=250)
    description = RichTextField(blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)
    external_link = models.CharField(max_length=250, blank=True)

    objects = ProductManager()

    def display_img_preview(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.display_img))
    display_img_preview.short_description = 'Display Image Preview'
    display_img_preview.allow_tags = True

    def __str__(self):
        return self.name
