# Generated by Django 4.1.7 on 2023-03-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment_status',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='payment_status',
            name='mode_of_payment',
        ),
        migrations.RemoveField(
            model_name='payment_status',
            name='price',
        ),
        migrations.RemoveField(
            model_name='payment_status',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='payment_status',
            name='quantity',
        ),
        migrations.AddField(
            model_name='payment_status',
            name='order_id',
            field=models.IntegerField(default=1),
        ),
    ]
