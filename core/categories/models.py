from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name'),
        ]
