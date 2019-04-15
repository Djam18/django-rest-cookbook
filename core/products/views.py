from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'stock']
    search_fields = ['name']
    ordering_fields = ['price', 'created', 'stock']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
