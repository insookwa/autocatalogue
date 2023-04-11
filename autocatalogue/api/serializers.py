
from rest_framework import serializers
from .models import *



#http://127.0.0.1:8000/acc/brand
class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


 #http://127.0.0.1:8000/acc/brand  Post service
class BrandPostSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length = None, use_url=True)
    class Meta:
        model = Brand
        fields = ('id','name','logo',)

    def create(self, validated_data):
            return Brand.objects.create(**validated_data)       


#http://127.0.0.1:8000/acc/model
class ModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Model
        fields = '__all__'

#http://127.0.0.1:8000/acc/generation
class GenerationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Generation
        fields = '__all__'


#http://127.0.0.1:8000/Car
class CarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Car
        fields = '__all__'

#http://127.0.0.1:8000/categories
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'

#http://127.0.0.1:8000/parts
class PartsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Part
        fields = '__all__'
