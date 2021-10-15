# Generated by Django 3.2.8 on 2021-10-14 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0005_auto_20211014_1345'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('order_id', models.CharField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_delivery', to='orders.delivery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]