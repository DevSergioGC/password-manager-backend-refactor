from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'min_length': 8,
                'style': {'input_type': 'password'}
            },
            'first_name': {'required': True},
            'last_name': {'required': False},
            'username': {'required': True, 'min_length': 5, 'max_length': 30},
            'email': {'required': True},
        }
    
    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError(
                {'username': 'Username already registered'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError(
                {'email': 'Email already registered'})
        return data
