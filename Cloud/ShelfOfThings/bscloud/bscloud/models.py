__author__ = 'Victor Polevoy'

from django.db import models


class Products(models.Model):
    board_id = models.CharField(max_length=200, null=False, blank=False)
    product_id = models.CharField(max_length=200, null=False, blank=False)


class Product(models.Model):
    product_id = models.CharField(max_length=200, null=False, blank=False)
    additional_info = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)