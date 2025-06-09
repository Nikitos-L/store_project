from rest_framework import generics, permissions, viewsets

from subscriptions.models import UserSubscriptions, Tariffs
from subscriptions.permissions import IsUserOrReadOnly
from subscriptions.serializers import TariffsSerializer, UserSubscriptionsSerializer


# Create your views here.
class TariffsAPIList(generics.ListCreateAPIView):
    queryset = Tariffs.objects.all()
    serializer_class = TariffsSerializer


class UserSubscriptionsAPIViewSet(viewsets.ModelViewSet):
    queryset = UserSubscriptions.objects.all()
    serializer_class = UserSubscriptionsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class UserSubscriptionsAPIList(generics.ListCreateAPIView):
#     queryset = UserSubscriptions.objects.all()
#     serializer_class = UserSubscriptionsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
#
# class UserSubscriptionsAPIDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserSubscriptions.objects.all()
#     serializer_class = UserSubscriptionsSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)