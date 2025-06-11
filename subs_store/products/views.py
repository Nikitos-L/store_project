from rest_framework import viewsets, permissions

from products.models import Orders
from products.serializers import OrdersSerializer


# Create your views here.
class OrdersAPIViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.username == 'admin':
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user.id)