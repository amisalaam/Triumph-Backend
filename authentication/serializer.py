from rest_framework import serializers
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
