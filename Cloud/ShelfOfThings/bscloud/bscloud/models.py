__author__ = 'Victor Polevoy'

from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
    additional_info = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)


class Board(models.Model):
    board_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
    board_name = models.CharField(max_length=200, null=False, blank=False)


class Products(models.Model):
    product_id = models.ForeignKey(Product, 'product_id')
    board_id = models.ForeignKey(Board, 'board_id')


class Jobs(models.Model):
    # product_id = models.CharField(max_length=200, null=False, blank=False)
    # board_id = models.CharField(max_length=200, null=False, blank=False)
    # dont needed:
    # board_id = models.ForeignKey(Board, 'board_id')
    product_id = models.ForeignKey(Product, 'product_id')
    job_type = models.PositiveIntegerField(null=False, blank=False)