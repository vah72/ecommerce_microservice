from django.db import models

class Order(models.Model):
    username = models.CharField(max_length=50)
    product_id = models.CharField(max_length=10)
    total = models.FloatField()
    shipment_id = models.IntegerField(default=1)

