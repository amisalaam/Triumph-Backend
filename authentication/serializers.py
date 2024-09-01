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
        user = User.objects.create_user(
            email=validated_data['email'],
            fullName=validated_data['fullName'],
            password=validated_data['password']
        )
        return user

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Password must be at least 6 characters long.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return value

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

        tokens = user.tokens()

        return {
            'refresh': tokens['refresh'],
            'access': tokens['access'],
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.fullName,
                'is_superuser': user.is_superuser,
            }
        }
