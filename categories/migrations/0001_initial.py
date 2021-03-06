# Generated by Django 3.1.7 on 2021-04-17 00:00

import categories.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_img', models.ImageField(upload_to=categories.models.category_dir_path)),
                ('description', models.TextField(blank=True)),
                ('youtube_link', models.CharField(blank=True, max_length=250)),
                ('external_link', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=categories.models.gallery_dir_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]
