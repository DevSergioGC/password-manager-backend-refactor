from django.urls import path, include
from .views import *

urlpatterns = [
    path('folders/', FolderView.as_view()),
    path('folders/<int:pk>/', DetailFolderView.as_view()),
    path('items/', ItemView.as_view()),
    path('items/<int:pk>/', DetailItemView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('register/', UserRegisterView.as_view()),
]
