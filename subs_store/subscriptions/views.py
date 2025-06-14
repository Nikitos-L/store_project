from rest_framework import generics, permissions, viewsets

from subscriptions.models import UserSubscriptions, Tariffs
from subscriptions.serializers import TariffsSerializer, UserSubscriptionsSerializer


# Create your views here.
class TariffsAPIList(generics.ListCreateAPIView):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer


class UserSubscriptionsAPIViewSet(viewsets.ModelViewSet):
    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if self.request.user.username == 'admin':
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user.id)