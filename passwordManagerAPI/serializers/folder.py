from rest_framework import serializers
from passwordManagerAPI.models import Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

        extra_kwargs = {
            'user': {'required': False}
        }