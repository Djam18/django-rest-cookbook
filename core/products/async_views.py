"""Experimental async views — Django 3.2 feature exploration.

Note: DRF doesn't support async natively yet. These are plain Django async views.
"""
from django.http import JsonResponse
from .models import Product


async def product_count(request):
    """Async view returning total product count.

    Django 3.2 supports async views — experimenting here.
    Not yet integrated with DRF serializers.
    """
    # sync_to_async needed for ORM calls in async context
    from asgiref.sync import sync_to_async
    count = await sync_to_async(Product.objects.count)()
    return JsonResponse({"count": count})
