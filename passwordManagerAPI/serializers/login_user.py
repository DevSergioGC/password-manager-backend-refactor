from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'min_length': 8,
                'style': {'input_type': 'password'}
            },
            'username': {'required': True, 'min_length': 5, 'max_length': 30},
        }

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            {'username': 'Invalid credentials'})
