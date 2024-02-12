from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # Django 3.1: JSONField now works with SQLite too (no longer PostgreSQL-only)
    metadata = models.JSONField(default=dict, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # Django 5.0: db_default — database-level default (no Python round-trip)
    is_featured = models.BooleanField(db_default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name='price_positive'),
            models.CheckConstraint(check=models.Q(stock__gte=0), name='stock_non_negative'),
        ]
