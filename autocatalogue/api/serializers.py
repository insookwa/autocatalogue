
from rest_framework import serializers
from .models import *



#http://127.0.0.1:8000/api/brand
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


 #http://127.0.0.1:8000/api/brand  Post service
class BrandPostSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Brand
        fields = ('id','name','logo')

    def create(self, validated_data):
            return Brand.objects.create(**validated_data)       


#http://127.0.0.1:8000/api/model
class ModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Model
        fields = '__all__'

#http://127.0.0.1:8000/api/generation
class GenerationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Generation
        fields = '__all__'


#http://127.0.0.1:8000/api/Car
class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'


#http://127.0.0.1:8000/api/Car  Post service

class CarPostSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Car
        fields = ('id','name','photo','brand','model','Generation','description')

    def create(self, validated_data):
            return Car.objects.create(**validated_data)   

#http://127.0.0.1:8000/categories  get service
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


#http://127.0.0.1:8000/api/categories  Post service
class CategoryPostSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Category
        fields = ('id','name','photo')

    def create(self, validated_data):
            return Category.objects.create(**validated_data)       


#http://127.0.0.1:8000/parts
class PartsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Part
        fields = '__all__'

class FavouriteCarSerializer(serializers.ModelSerializer):
     
     class Meta:
          model = FavoriteCar
          fields = ['favourite_car','created_at','updated_at']
          