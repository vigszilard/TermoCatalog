# Generated by Django 3.1.7 on 2021-04-26 05:10

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='display_img',
            field=models.ImageField(help_text='Dimenxiuni recomandate: ', upload_to=categories.models.category_dir_path),
        ),
    ]
