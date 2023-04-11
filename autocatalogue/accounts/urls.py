from .views import *
from django.urls import path

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('email-verify/',VerifyEmail.as_view(), name='email-verify'),
    path('login/',LoginAPIView.as_view(), name='login'),


]
