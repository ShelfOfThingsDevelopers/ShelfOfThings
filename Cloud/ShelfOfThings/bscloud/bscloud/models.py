__author__ = 'Victor Polevoy'

from django.db import models


class Product(models.Model):
    product_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
    additional_info = models.CharField(max_length=2000)
    name = models.CharField(max_length=200)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        product = Products.create(self.product_id)
        super().save(force_insert, force_update, using, update_fields)


class Board(models.Model):
    board_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
    board_name = models.CharField(max_length=200, null=False, blank=False)

    @classmethod
    def create(cls, board_id, board_name='Unnamed board'):
        board = cls(board_id=board_id, board_name=board_name)
        # do something with the book
        return board


class Products(models.Model):
    board_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
    product_id = models.CharField(max_length=200, null=False, blank=False)


    @classmethod
    def create(cls, board_id, product_id):
        product = cls(board_id=board_id, product_id=product_id)
        # do something with the book
        return product
    # product_id = models.ForeignKey(Product, 'product_id')
    # board_id = models.ForeignKey(Board, 'board_id')


class Jobs(models.Model):
    product_id = models.CharField(max_length=200, null=False, blank=False)
    # board_id = models.CharField(max_length=200, null=False, blank=False)
    # dont needed:
    # board_id = models.ForeignKey(Board, 'board_id')
    # product_id = models.ForeignKey(Product, 'product_id')
    job_type = models.PositiveIntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False, blank=True)
