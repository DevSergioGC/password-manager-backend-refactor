from passwordManagerAPI.models import Folder
from django.contrib.auth.models import User
from passwordManagerAPI.serializers import FolderSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import Token
from django.http import Http404
from rest_framework.response import Response


# @login_required
class FolderView(APIView):

    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

    def get(self, request):
        folder = Folder.objects.filter(user=request.user.id)
        serializer = FolderSerializer(folder, many=True)

        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            folder = Folder.objects.create(
                name=data['name'], user=request.user)
            folder.save()
            serializer = FolderSerializer(folder)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# @login_required
class DetailFolderView(APIView):
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
