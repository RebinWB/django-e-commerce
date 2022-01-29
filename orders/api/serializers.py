from rest_framework import serializers
from orders.models import Order, Cart, OrderDetails


class OrderSerializer(serializers.ModelSerializer):
    """
    users order serializer
    """
    class Meta:
        model = Order
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    """
    users cart serializer (each cart contain some of a product)
    """
    class Meta:
        model = Cart
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    order delivery details serializer
    """
    class Meta:
        model = OrderDetails
        fields = "__all__"

