from django.urls import path,include

from .views import *

urlpatterns = [
        path('GetCustomers/', GetCustomers.as_view()),
        path('AddCustomers/', AddCustomers.as_view()),
        path('DeleteCustomers/', DeleteCustomer.as_view()),
        path('UpdateCustomer/', UpdateCustomer.as_view()),
        path('Login/', Login.as_view()),
        path('GenerateOTPChangePassword/', GenerateOTPChangePassword.as_view()),
        path('VerifyOtpChangePassword/', VerifyOtpChangePassword.as_view()),
        path('ChangePassword/',ChangePassword.as_view())

]
