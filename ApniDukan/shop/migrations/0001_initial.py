# Generated by Django 2.2.4 on 2020-03-25 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('with_product', models.IntegerField()),
                ('get_product', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'discount_code',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount', models.ForeignKey(null=True, on_delete=False, to='shop.DiscountCode')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cartId', models.ForeignKey(on_delete=False, to='shop.Cart')),
                ('product', models.ForeignKey(on_delete=False, to='shop.Product')),
            ],
            options={
                'db_table': 'cart_item',
            },
        ),
    ]