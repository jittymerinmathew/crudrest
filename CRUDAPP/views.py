from rest_framework import generics
from rest_framework.response import Response
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['PUT'])
def activate_or_deactivate_product(request, product_id, action):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Check if the product is registered more than 2 months ago
    if product.registration_date < timezone.now() - timedelta(days=60):
        if action == 'activate':
            product.is_active = True
        elif action == 'deactivate':
            product.is_active = False
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Invalid action'})

        product.save()

        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Product cannot be deactivated as it was registered within the last 2 months'})
