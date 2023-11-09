from passwordManagerAPI.models import Folder
from django.contrib.auth.models import User
from passwordManagerAPI.serializers import UserSerializer, UserLoginSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.response import Response


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({"data": user}, status=status.HTTP_202_ACCEPTED)


class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'detail': 'Successfully logged out.'})


class UserRegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        user = request.data
        serializer = UserSerializer(data=user)

        if serializer.is_valid():
            new_user = User.objects.create(
                first_name=user['first_name'], last_name=user['last_name'], username=user['username'], email=user['email']
            )
            new_user.set_password(user['password'])
            new_user.save()

            # ? Create 'default' folder related to created user
            new_folder = Folder.objects.create(
                name='Default', user=new_user)
            new_folder.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
