# Generated by Django 3.1.7 on 2023-03-04 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20230304_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='photo_1',
            field=models.ImageField(upload_to='photos/about/'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='photo_2',
            field=models.ImageField(upload_to='photos/about/'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to='photos/about/partners/'),
        ),
    ]
