"""
ASGI config for core project.

Exposes the ASGI callable as a module-level variable named ``application``.
Django 3.0 introduces ASGI support.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
