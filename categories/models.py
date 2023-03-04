from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
import os

def category_dir_path(instance, filename):
    return os.path.join('photos/', instance.name, filename)

def gallery_dir_path(instance, filename):
    return os.path.join('photos/', instance.category.name, filename)

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().order_by('relevance', 'name')

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)
    display_img = models.CharField(max_length=250)
    description = RichTextField()
    youtube_link = models.CharField(max_length=250, blank=True)
    external_link = models.CharField(max_length=250, blank=True)
    relevance = models.PositiveIntegerField(default=2, validators=[MinValueValidator(1), MaxValueValidator(5)])

    sorted_by_relevance = CategoryManager()

    def display_img_preview(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.display_img))
    display_img_preview.short_description = 'Display Image Preview'
    display_img_preview.allow_tags = True

    def __str__(self):
        return self.name

class Gallery(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photo =  models.CharField(max_length=250)

    def __str__(self):
        return self.category.name
        