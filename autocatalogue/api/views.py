
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView


#Cars View 
class CarsAPIView(APIView):
    def get(self,request,format=None):
        res  = Car.objects.all()
        serializer =CarSerializer(res ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        
        data = {
                'name' : request.data.get('name'),
                'logo' : request.data['logo'],
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
                'logo' : request.data.get('file'),
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
        Res= Model.objects.all()
        serializer = ModelSerializer(Res,many=True)
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
        Res = Generation.objects.all()
        serializer = GenerationSerializer(Res,many=True)
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
        Res = Category.objects.all()
        serializer = CategorySerializer(Res,many=True)
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
        Res = Part.objects.all()
        serializer = PartsSerializer(Res,many=True)
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



