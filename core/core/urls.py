from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from products.async_views import product_count, product_detail_async

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token),
    # Django 4.1 async views
    path('api/products/count/', product_count, name='product-count-async'),
    path('api/products/<int:pk>/async/', product_detail_async, name='product-detail-async'),
    # drf-spectacular: OpenAPI schema + Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
