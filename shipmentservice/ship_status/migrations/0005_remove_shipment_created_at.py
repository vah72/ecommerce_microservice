# Generated by Django 4.1.7 on 2023-03-30 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ship_status', '0004_alter_shipment_order_id_alter_shipment_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='created_at',
        ),
    ]
