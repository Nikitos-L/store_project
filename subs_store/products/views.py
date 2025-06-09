from rest_framework import generics, viewsets

from products.models import Orders
from products.serializers import OrdersSerializer


# Create your views here.
class OrdersAPIViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class OrdersAPIList(generics.ListCreateAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer
#
#
# class OrdersAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer