from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from products.async_views import product_count, product_detail_async

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token),
    # Django 4.1 async views
    path('api/products/count/', product_count, name='product-count-async'),
    path('api/products/<int:pk>/async/', product_detail_async, name='product-detail-async'),
]
