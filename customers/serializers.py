from rest_framework import serializers
from .models import Customers


class CustomersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=30)
    category = serializers.CharField(max_length=30)
    payment_type = serializers.CharField(max_length=30)

    class Meta:
        model = Customers
        fields = '__all__'


class CommomResponseSerializer(serializers.Serializer):
    state = serializers.CharField(max_length=30)
    msg = serializers.CharField(max_length=30)
