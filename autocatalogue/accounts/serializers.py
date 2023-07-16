from rest_framework import serializers
from .models import *
#from django.contrib import auth
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length =6 , write_only=True
    )
    
    class Meta:
        model=User
        fields = ['email','username','password']
    
    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters ')
        
        return attrs
    
# def create(self,validate_data):
#     user =  User.objects.create_user(**validate_data)
#     user.set_password(validate_data.get('password'))
#     user.save()
#     return user



class EmailVarificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length = 555)

    class Meta:
        model = User
        fields = ['token']

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length =3 )
    password = serializers.CharField(max_length=68,min_length =6,write_only =True)
    username = serializers.CharField(max_length=255,min_length =2,read_only = True)
    tokens = serializers.CharField(max_length=68,min_length =6,read_only = True)


    class Meta:
        model = User
        fields = ['email','password','username','tokens']

    def validate(self,attrs):
        super().validate(attrs)
        email = attrs.get('email','')
        password = attrs.get('password','')

        user = authenticate(email=email,password=password)

        # return super().validate(attrs)

        return{

            'email':user.email,
            'username':user.username,
            'tokens':user.tokens

        }
        

