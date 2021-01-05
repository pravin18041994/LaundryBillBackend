from rest_framework import serializers
from .models import Shops


class ShopsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    address = serializers.CharField(max_length=30)
    owner_name = serializers.CharField(max_length=30)

    class Meta:
        model = Shops
        fields = '__all__'


class CommonResponseSerializer(serializers.Serializer):
    state = serializers.CharField(max_length=30)
    msg = serializers.CharField(max_length=30)
