from django.shortcuts import render
from rest_framework.views import APIView
from .models import Customers
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomersSerializer
import random


# Create your views here.
class GetCustomers(APIView):
    def get(self, request):
        usernames = Customers.objects.all()
        serializer = CustomersSerializer(data=usernames, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddCustomers(APIView):
    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCustomer(APIView):
    def post(self, request):
        instance = Customers.objects.get(id=request.POST.get('id'))
        serializer = CustomersSerializer(data=instance)
        instance.delete()
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class UpdateCustomer(APIView):
    def post(self, request):
        instance = Customers.objects.filter(id=request.POST.get('id'))
        print(instance)
        serializer = CustomersSerializer(data=instance, many=True)
        for object in instance:
            object.name = request.POST.get('name')
            object.contact = request.POST.get('contact')
            object.email = request.POST.get('email')
            object.address = request.POST.get('address')
            object.category = request.POST.get('category')
            object.payment_type = request.POST.get('payment_type')
            object.save()

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class Login(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        valid_contact = Customers.objects.filter(contact=contact)
        print(valid_contact)
        if (len(valid_contact)) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Customers.objects.filter(contact=contact, password=password)
        if len(valid_user) == 1:
            return Response({'state': 'success', 'msg': 'login successful '})
        else:
            return Response({'state': 'fail', 'msg': 'invalid credentials'})


class GenerateOTPChangePassword(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        valid_contact = Customers.objects.filter(contact=contact)
        print(valid_contact)
        if (len(valid_contact)) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Customers.objects.filter(contact=contact)
        if len(valid_user) == 1:
            otp = random.randint(1000, 9999)
            print(otp)
            user = Customers.objects.get(contact=contact)
            user.verification_otp = otp
            user.save()
        return Response({'state': 'success', 'msg': 'Otp sent !'})


class VerifyOtpChangePassword(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        otp = request.POST.get('otp')
        valid_contact = Customers.objects.filter(contact=contact)
        print(valid_contact)
        if (len(valid_contact)) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Customers.objects.filter(contact=contact)
        if len(valid_user) == 1:
            user = Customers.objects.get(contact=contact)
            if user.verification_otp == otp:
                return Response({'state': 'success', 'msg': 'Otp verified !'})
            else:
                return Response({'state': 'fail', 'msg': 'invalid Otp  !'})
        return Response({'msg': 'bad request '}, status=status.HTTP_400_BAD_REQUEST)

class ChangePassword(APIView):
    def post(self, request):
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        valid_contact = Customers.objects.filter(contact=contact)
        print(valid_contact)
        if (len(valid_contact)) == 0:
            return Response({'state': 'fail', 'msg': 'contact not registered'})
        valid_user = Customers.objects.filter(contact=contact)
        if len(valid_user) == 1:
            user = Customers.objects.get(contact=contact)
            user.password = password
            user.save()
            return Response({'state': 'success', 'msg': 'Password updated !'})
        return Response({'msg': 'bad request '}, status=status.HTTP_400_BAD_REQUEST)



