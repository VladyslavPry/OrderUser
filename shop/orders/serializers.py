from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer
from products.serializers import ProductSerializer 

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    products = ProductSerializer(read_only=True, many=True)

    class Meta:
        order = Order
        fields = '__all__'
