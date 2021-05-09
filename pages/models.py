from django.db import models
from django.db.models import ImageField, TextField, CharField, EmailField
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

    class Meta:
        verbose_name_plural = 'aboutPage'

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'About page details'

class Partner(models.Model):
    name = CharField(max_length=100)
    logo = ImageField(upload_to='photos/about/partners/')

    def __str__(self):
        return self.name

class ContactPage(models.Model):
    street_name = CharField(max_length=100)
    street_number = CharField(max_length=20, blank=True)
    unit = CharField(max_length=20, blank=True)
    entrance = CharField(max_length=20, blank=True)
    city = CharField(max_length=100)
    region = CharField(max_length=100)
    country = CharField(max_length=100)
    zip_code = CharField(max_length=6, blank=True)
    landline = CharField(max_length=20, blank=True)
    fax = CharField(max_length=20, blank=True)
    mobile = CharField(max_length=20, blank=True)
    email = EmailField()
    schedule = TextField()

    class Meta:
        verbose_name_plural = 'contactPage'

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Contact page details'

class FAQPage(models.Model):
    question = TextField()
    answer = TextField()

    class Meta:
        verbose_name_plural = 'faqPage'
        verbose_name = 'faq'

    def __str__(self):
        return 'FAQ page details'