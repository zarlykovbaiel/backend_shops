# Generated by Django 3.2.8 on 2021-10-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20211013_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='users',
        ),
    ]
