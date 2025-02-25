from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'profile', 'password']
        extra_kwargs = {'password': {'write_only': True}, 'profile': {'required': False}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid login credentials")
        # Check if user is active
        if not user.is_active:
            raise serializers.ValidationError("This user account is inactive.")
        return {'user': user}