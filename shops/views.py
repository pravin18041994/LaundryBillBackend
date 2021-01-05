import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Shops
from .serializers import *


# Create your views here.
class GetShops(APIView):
    def get(self, request):
        usernames = Shops.objects.all()
        serializer = ShopsSerializer(data=usernames, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddShops(APIView):
    def post(self, request):
        serializer = ShopsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteShop(APIView):
    def post(self, request):
        instance = Shops.objects.get(id=request.POST.get('id'))
        serializer = ShopsSerializer(data=instance)
        instance.delete()
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class UpdateShops(APIView):
    def post(self, request):
        instance = Shops.objects.filter(id=request.POST.get('id'))
        serializer = ShopsSerializer(data=instance, many=True)
        for object in instance:
            object.name = request.POST.get('name')
            object.contact = request.POST.get('contact')
            object.email = request.POST.get('email')
            object.address = request.POST.get('address')
            object.owner_name = request.POST.get('owner_name')
            object.save()

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class Login(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        valid_contact = Shops.objects.filter(contact=contact)
        print(valid_contact)
        if len(valid_contact) == 0:
            return Response({'state': 'fail', 'msg': 'Contact not registered'})
        valid_user = Shops.objects.filter(contact=contact, password=password)
        if len(valid_user) == 1:
            return Response({'state': 'success', 'msg': 'Login successful'})
        else:
            return Response({'state': 'fail', 'msg': 'Invalid credentials'})


class GenerateOtp(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        valid_contact = Shops.objects.filter(contact=contact)
        print(valid_contact)
        if len(valid_contact) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Shops.objects.filter(contact=contact)
        if len(valid_user) == 1:
            otp = random.randint(1000, 9999)
            print(otp)
            user = Shops.objects.get(contact=contact)
            user.verification_otp = otp
            user.save()
        return Response({'state': 'success', 'msg': 'Otp sent !'})


class VerifyOtp(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        otp = request.POST.get('otp')
        valid_contact = Shops.objects.filter(contact=contact)
        print(valid_contact)
        if len(valid_contact) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Shops.objects.filter(contact=contact)
        if len(valid_user) == 1:
            user = Shops.objects.get(contact=contact)
            if user.verification_otp == otp:
                return Response({'state': 'success', 'msg': 'otp verified'})
            else:
                return Response({'state': 'fail', 'msg': 'invalid otp'})
        return Response({'msg': 'bad request '}, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):
    def post(self, req):
        contact = req.POST.get('contact')
        password = req.POST.get('password')
        valid_contact = Shops.objects.filter(contact=contact)
        print(valid_contact)
        if len(valid_contact) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Shops.objects.filter(contact=contact)
        if len(valid_user) == 1:
            user = Shops.objects.get(contact=contact)
            user.password = password
            user.save()
            return Response({'state': 'success', 'msg': 'password updated !'})
        return Response({'msg': 'bad request '}, status=status.HTTP_400_BAD_REQUEST)
