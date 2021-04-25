# Generated by Django 3.1.7 on 2021-04-24 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210424_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(blank=True, max_length=20)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('entrance', models.CharField(blank=True, max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(blank=True, max_length=6)),
                ('landline', models.CharField(blank=True, max_length=20)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('schedule', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'contactPage',
            },
        ),
    ]
