from django.db import models
import os

def category_dir_path(instance, filename):
    return os.path.join('photos/', instance.name, filename)

def gallery_dir_path(instance, filename):
    return os.path.join('photos/', instance.category.name, filename)

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)
    display_img = models.ImageField(upload_to=category_dir_path)
    description = models.TextField(blank=True)
    youtube_link = models.CharField(max_length=250, blank=True)
    external_link = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=gallery_dir_path)

    def __str__(self):
        return self.category.name
