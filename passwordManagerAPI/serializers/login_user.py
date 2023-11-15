from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True, min_length=5, max_length=30)
    password = serializers.CharField(
        write_only=True, required=True, min_length=8, style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        request = self.context.get('request')

        user = authenticate(
            request=request, username=username, password=password)

        if user and user.is_active:
            return user

        raise serializers.ValidationError(
            {'username': 'Invalid credentials'})
