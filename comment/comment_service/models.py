
from __future__ import unicode_literals
from django.db import models
class product_comment(models.Model):
    comment = models.TextField()
    rating = models.IntegerField() #one to five star
    created_date = models.DateTimeField(auto_now_add=True)
    # user_id = models.IntegerField()
    # product_id = models.IntegerField()
    uname = models.CharField(max_length=250)
    product_id = models.CharField(max_length=250)
    product_name = models.CharField(max_length=250)
    # orderitem_id = models.IntegerField()