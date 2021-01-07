from rest_framework import serializers

from shopWorker.models import ShopWorker


class ShopWorkerSerializers(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    contact = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    fcm_token = serializers.CharField(max_length=30)

    class Meta:
        model = ShopWorker,
        fields = '__all__'


class CommonResponseSerializer(serializers.Serializer):
    state = serializers.CharField(max_length=30)
    msg = serializers.CharField(max_length=30)
