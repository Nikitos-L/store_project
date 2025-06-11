from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import OrdersAPIViewSet

router = DefaultRouter()
router.register(r'orders', OrdersAPIViewSet)

urlpatterns = [
    path('', include(router.urls))
]