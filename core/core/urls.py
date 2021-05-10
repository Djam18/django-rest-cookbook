from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from products.async_views import product_count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token),
    # Django 3.2 async view experiment
    path('api/products/count/', product_count, name='product-count-async'),
]
