# Generated by Django 3.1.7 on 2023-01-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20220416_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='display_img',
            field=models.CharField(max_length=250),
        ),
    ]
