from django.db import models
from django.db.models import ImageField
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and obj.id != model.objects.get().id):
        raise ValidationError("Can only create 1 %s instance" % model.__name__)


class AboutPage(models.Model):
    photo_1 = ImageField(upload_to='photos/about/')
    photo_2 = ImageField(upload_to='photos/about/')
    content = RichTextField()

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'About page'