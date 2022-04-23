import os

from django.db import models
from django.utils.safestring import mark_safe


def product_dir_path_sb(instance, filename):
    return os.path.join('photos/designs/sandblast', filename)


class SandblastManager(models.Manager):
    def get_queryset(self):
        return super(SandblastManager, self).get_queryset().order_by('wide', 'high', 'name')


class Sandblast(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_dir_path_sb)
    wide = models.BooleanField(default=False)
    high = models.BooleanField(default=False)

    sorted_by_size = SandblastManager()

    def display_img_preview(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    display_img_preview.short_description = 'Display Image Preview'
    display_img_preview.allow_tags = True

    def __str__(self):
        return self.name


def product_dir_path_pr(instance, filename):
    return os.path.join('photos/designs/sandblast', filename)


class PrintingManager(models.Manager):
    def get_queryset(self):
        return super(PrintingManager, self).get_queryset().order_by('wide', 'high', 'name')


class Printing(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_dir_path_pr)
    wide = models.BooleanField(default=False)
    high = models.BooleanField(default=False)

    sorted_by_size = PrintingManager()

    def display_img_preview(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))

    display_img_preview.short_description = 'Display Image Preview'
    display_img_preview.allow_tags = True

    def __str__(self):
        return self.name
