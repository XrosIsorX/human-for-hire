# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from post.models import Product
import datetime

# Create your models here.
class Order(models.Model):
    order_no = models.IntegerField(primary_key=True)
    product_no = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    buyer_username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    purchase_date = models.DateTimeField(default=datetime.datetime.now())
    location = models.CharField(max_length=250, default='location')
    price = models.IntegerField(default=0)
    detail = models.CharField(max_length=250, default='datail')
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now())
    #status_code = models.

    def __str__(self):
        return str(self.product_no) + "_" + self.product_name