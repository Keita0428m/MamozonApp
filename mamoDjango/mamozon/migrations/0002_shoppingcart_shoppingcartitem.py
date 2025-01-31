# Generated by Django 3.0.7 on 2020-06-16 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mamozon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='mamozon.User', verbose_name='ユーザ')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='数量')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='mamozon.ShoppingCart', verbose_name='ショッピングカート')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamozon.Product', verbose_name='商品')),
            ],
        ),
    ]
