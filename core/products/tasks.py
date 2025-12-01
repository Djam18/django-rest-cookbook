"""Background tasks — Django 6.0 native (no Celery needed for simple jobs).

Django 6.0 introduced background tasks that run after the HTTP response
is sent, using the WSGI/ASGI server's thread pool. No broker required.

Usage:
    from django.tasks import background_task

    @background_task
    def send_low_stock_alert(product_id: int) -> None:
        ...

    # In a view — runs after response is sent to client:
    send_low_stock_alert.enqueue(product.pk)
"""
from __future__ import annotations

import logging

from django.core.mail import send_mail

logger = logging.getLogger(__name__)


# Django 6.0 native background task
try:
    from django.tasks import background_task  # type: ignore[import]

    @background_task
    def send_low_stock_alert(product_id: int) -> None:
        """Notify admin when a product drops below minimum stock threshold."""
        from .models import Product

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            logger.warning("send_low_stock_alert: product %d not found", product_id)
            return

        send_mail(
            subject=f"Low stock alert: {product.name}",
            message=f"Product '{product.name}' has only {product.stock} units left.",
            from_email="noreply@cookbook.example.com",
            recipient_list=["admin@cookbook.example.com"],
            fail_silently=True,
        )
        logger.info("Low stock alert sent for product %d", product_id)

except ImportError:
    # Fallback for Django < 6.0
    def send_low_stock_alert(product_id: int) -> None:  # type: ignore[misc]
        logger.info("Background tasks not available (Django < 6.0), running synchronously")
