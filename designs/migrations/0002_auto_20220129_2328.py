# Generated by Django 3.1.7 on 2022-01-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sandblast',
            name='high',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sandblast',
            name='wide',
            field=models.BooleanField(default=False),
        ),
    ]
