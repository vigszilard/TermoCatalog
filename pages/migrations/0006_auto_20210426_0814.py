# Generated by Django 3.1.7 on 2021-04-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_answer_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'answer'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'question', 'verbose_name_plural': 'faqPage'},
        ),
    ]