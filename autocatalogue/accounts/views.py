from django.urls import reverse
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.views import APIView


class RegisterView(generics.GenericAPIView):
    serializer_class=RegisterSerializer


    def post(self,request):
        user = request.data
        serializer=self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = User.objects.get(email = user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')
        absurl = 'http://'+current_site+relativeLink+"?token"+str(token)
        email_body = 'Hi '+user.username+'Use link below to verify your email \n'+absurl
        data = {'email_body':email_body,'to_email':user.email,'email_subject':'Verify your email'}
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass

#Cars View 
class CarsAPIView(APIView):
    def get(self,request,format=None):
        response  = Car.objects.all()
        serializer =CarSerializer(response ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        
        data = {
                'name' : request.data.get('name'),
                'logo' : request.data['file'],
                'brand' : request.data.get('brand'),
                'model' : request.data.get('model'),
                'Generation' : request.data.get('Generation'),
                'description' : request.data.get('description'),   
 
        }

        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Brands View 
class BrandsAPIView(APIView):

    def get(self,request):
        res = Brand.objects.all()
        print(res)
        serializer = BrandSerializer(res,many=True)

        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
                'logo' : request.data.get('logo'),
                'created_at' : request.data.get('created_at'),
                'update_at' : request.data.get('update_at'),
                
        }

        serializer = BrandPostSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Models View 
class ModelsAPIView(APIView):
    def get(self,request,format=None):
        Response = Model.objects.all()
        serializer = ModelSerializer(Response,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
                'brand' : request.data.get('brand'),
                'created_at' : request.data.get('created_at'),
                'update_at' : request.data.get('update_at'),
                
        }
        serializer = ModelSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Generations View 
class GenerationsAPIView(APIView):
    def get(self,request,format=None):
        Response = Generation.objects.all()
        serializer = GenerationSerializer(Response,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),
                'model' : request.data.get('model'),
                'created_at' : request.data.get('created_at'),
                'update_at' : request.data.get('update_at'),
        }
        serializer = GenerationSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Categories View 
class CategoriesAPIView(APIView):
    def get(self,request,format=None):
        Response = Category.objects.all()
        serializer = CategorySerializer(Response,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),

        }
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Parts View 
class PartsAPIView(APIView):
    def det(self,request,format=None):
        Response = Part.objects.all()
        serializer = PartsSerializer(Response,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.data.get('name'),

        }
        serializer = PartsSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


