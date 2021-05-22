# Generated by Django 3.1.7 on 2021-05-15 12:17

import categories.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20210515_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='relevance',
            field=models.PositiveIntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='display_img',
            field=models.ImageField(help_text='Dimensiuni recomandate: ', upload_to=categories.models.category_dir_path),
        ),
    ]