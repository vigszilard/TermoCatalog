# Generated by Django 3.1.7 on 2021-05-15 10:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210426_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]