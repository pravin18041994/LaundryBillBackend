from django.urls import path, include
from .views import *

urlpatterns = [
    path('GetShops/', GetShops.as_view()),
    path('AddShops/', AddShops.as_view()),
    path('DeleteShop/', DeleteShop.as_view()),
    path('UpdateShop/', UpdateShops.as_view()),
    path('Login/', Login.as_view()),
    path('GenerateOtp/', GenerateOtp.as_view()),
    path('VerifyOtp/', VerifyOtp.as_view()),
    path('ChangePassword/',ChangePassword.as_view())
]
