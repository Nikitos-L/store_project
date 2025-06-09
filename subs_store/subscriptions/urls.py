from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscriptions import views
from subscriptions.views import UserSubscriptionsAPIViewSet

router = DefaultRouter()
router.register(r'usersubs', UserSubscriptionsAPIViewSet)

urlpatterns = [
    path('tariffs/', views.TariffsAPIList.as_view()),
    path('', include(router.urls)),
    # path('usersubs/', views.UserSubscriptionsAPIList.as_view()),
    # path('usersubs/<int:pk>/', views.UserSubscriptionsAPIDetail.as_view())
]