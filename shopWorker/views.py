from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status



# Create your views here.

class AddShopWorker(APIView):

    def post(self, request):
        serializer = ShopWorkerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetShopWorker(APIView):
    def get(self, request):
        workername = ShopWorker.objects.all()
        serializer = ShopWorkerSerializers(data=workername, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteShopWorker(APIView):
    def post(self,request):
        instance=ShopWorker.objects.filter(id=request.POST.get('id'))
        serializer=ShopWorkerSerializers(data=instance)
        instance.delete()
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

class UpdateShopWorker(APIView):
    def post(self,request):
        instance=ShopWorker.objects.filter(id=request.POST.get('id'))
        serializer=ShopWorkerSerializers(data=instance,many=True)
        for object in instance:
            object.name=request.POST.get('name')
            object.contact = request.POST.get('contact')
            object.password = request.POST.get('password')
            object.fcm_token = request.POST.get('fcm_token')
            object.save()
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


