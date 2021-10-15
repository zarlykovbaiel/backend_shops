# Generated by Django 3.2.8 on 2021-10-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='nazvanie')),
                ('slug', models.SlugField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'kategorii',
            },
        ),
    ]
