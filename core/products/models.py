from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name='price_positive'),
            models.CheckConstraint(check=models.Q(stock__gte=0), name='stock_non_negative'),
        ]
