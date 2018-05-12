# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AddExpense(models.Model):

    Expensetitle = models.CharField(max_length=20)
    Amount = models.DecimalField(decimal_places=2, max_digits=10)
    Currency = models.CharField(max_length=23)
    PaymentType = models.CharField(max_length=30)
    ExpenseType = models.CharField(max_length=200)
    VendorName = models.CharField(max_length=200)