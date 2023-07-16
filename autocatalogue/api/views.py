
from rest_framework import generics, permissions,status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import permissions
from .permissions import IsOwner


#Cars View 
class CarsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,format=None):
        res  = Car.objects.all()
        serializer =CarSerializer(res ,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        
        data = {
                'name' : request.POST.get('name'),
                'photo' : request.FILES['photo'],
                'brand' : request.POST.get('brand'),
                'model' : request.POST.get('model'),
                'generation' : request.POST.get('generation'),
                'description' : request.POST.get('description'),
        }

        serializer = CarSerializer(data=data)
        
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Brands View 
class BrandsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        res = Brand.objects.all()
        print(res)
        serializer = BrandSerializer(res,many=True)

        return Response(serializer.data)
    
    def post(self,request,*args, **kwargs):


        data = {
                'name' : request.POST.get('name'),
                'logo' : request.FILES['logo'],   
        }

        serializer = BrandPostSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Models View 
class ModelsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,format=None):
        Res= Model.objects.all()
        serializer = ModelSerializer(Res,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):

        data = {
                'name' : request.POST.get('name'),
                'brand' : request.POST.get('brand'),
        }

        serializer = ModelSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Generations View 
class GenerationsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,format=None):
        Res = Generation.objects.all()
        serializer = GenerationSerializer(Res,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {

                'name' : request.POST.get('name'),
                'model' : request.POST.get('model'),
        }
        serializer = GenerationSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Categories View 
class CategoriesAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,format=None):
        Res = Category.objects.all()
        serializer = CategorySerializer(Res,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.POST.get('name'),

        }
        serializer = CategoryPostSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Parts View 
class PartsAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def det(self,request,format=None):
        Res = Part.objects.all()
        serializer = PartsSerializer(Res,many=True)
        return Response(serializer.data,status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        data = {
                'name' : request.POST.get('name'),

        }
        serializer = PartsSerializer(data=data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(obj.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FavouriteCarsAPIView(ListCreateAPIView):
    serializer_class = FavouriteCarSerializer
    queryset =FavoriteCar.objects.all()
    permission_classes = (permissions.IsAuthenticated,)




    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

class FavouriteCarsDetailAPIView(ListCreateAPIView):
    serializer_class = FavouriteCarSerializer
    queryset =FavoriteCar.objects.all()
    permission_classes = (permissions.IsAuthenticated,IsOwner)
    lookup_field = 'id'




    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(owner = self.request.user)

