from django.urls import reverse
from rest_framework import generics, permissions,status,views
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.views import APIView
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer


    def post(self,request):
        user = request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        u  = serializer.save()
        u.set_password(user.get('password'))
        u.save()
        user_data = serializer.data

        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        print(token)
        email_body = 'Hi '+user.username+'Use link below to verify your email \n'+absurl
        data = {'email_body':email_body,'to_email':user.email,'email_subject':'Verify your email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):
    serializer_class = EmailVarificationSerializer
    token_param_config = openapi.Parameter('token',in_=openapi.IN_QUERY,description='Введите токен, полученный после регистрации, для верификации пользователя',type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self,request):
        token = self.request.GET.get('token')
        try:
            print(f"token: {token}")

            payload = jwt.decode(token,settings.SECRET_KEY,algorithms=['HS256'])
            
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Sucessfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_200_OK)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token %s' % identifier}, status=status.HTTP_400_BAD_REQUEST)
        

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
