"""Async views — Django 4.1 async ORM support.

Django 4.1 adds async versions of ORM methods (acount, aget, afilter, etc.).
DRF doesn't support async natively yet, so these are plain Django views.
"""
from django.http import JsonResponse
from .models import Product


async def product_count(request):
    """Async view returning total product count.

    Django 4.1: can call ORM methods directly in async context.
    """
    # Django 4.1 async ORM: acount() instead of sync_to_async wrapper
    count = await Product.objects.acount()
    return JsonResponse({"count": count})


async def product_detail_async(request, pk):
    """Async detail view experiment.

    Django 4.1 supports aget() for single object retrieval.
    """
    try:
        product = await Product.objects.aget(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"error": "not found"}, status=404)

    return JsonResponse({
        "id": product.pk,
        "name": product.name,
        "price": str(product.price),
        "stock": product.stock,
    })
