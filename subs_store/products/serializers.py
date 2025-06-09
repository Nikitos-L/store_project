from rest_framework import serializers

from products.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Orders
        fields = '__all__'