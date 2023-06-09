# Generated by Django 4.1.7 on 2023-03-30 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_order_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='username',
        ),
        migrations.AddField(
            model_name='order',
            name='cart_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
