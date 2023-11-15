from passwordManagerAPI.models import Folder, Items
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


class FolderView(APIView):

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


class DetailFolderView(APIView):
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        folder = self.get_object(pk)
        default = Folder.objects.filter(user=self.request.user).first()
        item = Items.objects.filter(folder=folder).update(folder=default)
        folder.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
