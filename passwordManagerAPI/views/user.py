from passwordManagerAPI.models import Folder
from django.contrib.auth.models import User
from passwordManagerAPI.serializers import UserSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.views import Token
from django.http import Http404
from rest_framework.response import Response


class UserLoginView(APIView):
    def post(self, request):
        pass


class UserLogoutView(APIView):
    def post(self, request):
        pass


class UserRegisterView(APIView):
    def post(self, request, format=None):
        user = request.data
        serializer = UserSerializer(data=user)

        if serializer.is_valid():
            new_user = User.objects.create(
                first_name=user['first_name'], last_name=user['last_name'], username=user['username'], email=user['email']
            )
            new_user.set_password(user['password'])
            new_user.save()

            #? Create 'default' folder related to created user
            new_folder = Folder.objects.create(
                name='Default', user=new_user)
            new_folder.save()

            # ? Create a user's Token
            # Token.create(user=new_user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
