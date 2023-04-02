from rest_framework import serializers
from .models import *






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
    
def create(self,validate_data):
    return User.objects.create_user(**validate_data)



class EmailVarificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length = 555)

    class Meta:
        model = User
        fields = ['token']

