from passwordManagerAPI.models import Folder, Items
from passwordManagerAPI.serializers import FolderSerializer
from rest_framework import status
from rest_framework.views import APIView
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
        folder = Folder.objects.filter(
            user=self.request.user.id, pk=pk).first()

        if folder is None:
            raise Http404
        return folder

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

        if folder.verify_default_folder():
            return Response(status=status.HTTP_400_BAD_REQUEST, message='You cannot delete the default folder.')

        default = Folder.objects.filter(
            user=self.request.user, name='default').first()
        item = Items.objects.filter(
            folder=folder, user=self.request.user).update(folder=default)
        folder.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
