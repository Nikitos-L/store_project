from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import OrdersAPIViewSet

router = DefaultRouter()
router.register(r'orders', OrdersAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('orders/', OrdersAPIList.as_view()),
    # path('orders/<int:pk>/', OrdersAPIDetail.as_view())
]