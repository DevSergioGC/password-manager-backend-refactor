from rest_framework import serializers
from passwordManagerAPI.models import Items

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = "__all__"

        extra_kwargs = {
            'user': {'required': False},
            'folder': {'required': False},
            'description': {'required': False},
            'url': {'required': False},
        }
