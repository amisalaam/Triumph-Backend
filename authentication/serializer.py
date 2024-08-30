from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullName', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        # Create a new user instance with the validated data
        user = User.objects.create_user(
            email=validated_data['email'],
            fullName=validated_data['fullName'],
            password=validated_data['password']
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid login credentials')

        if not user.is_active:
            raise serializers.ValidationError('This account is inactive')

        return {
            'email': user.email,
            'fullName': user.fullName,
            'tokens': user.tokens()
        }