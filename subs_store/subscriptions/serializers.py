from django.conf import settings
from rest_framework import serializers

from subscriptions.models import Tariffs, UserSubscriptions, CustomUser


class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = '__all__'


class UserSubscriptionsSerializer(serializers.ModelSerializer):
    user =serializers.ReadOnlyField(source='user.username')
    # tariff = serializers.CharField(source='tariff.name_tariff')

    class Meta:
        model = UserSubscriptions
        fields = '__all__'


# class CustomUserSerializer(serializers.ModelSerializer):
#     subscriptions = serializers.PrimaryKeyRelatedField(many=True,
#                                                        queryset=UserSubscriptions.objects.all())
#
#     class Meta:
#         model = settings.AUTH_USER_MODEL
#         fields = ['id', 'username', 'subscriptions']