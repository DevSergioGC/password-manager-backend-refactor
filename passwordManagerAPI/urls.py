from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/v1/folders/', FolderView.as_view()),
    path('api/v1/folders/<int:pk>/', DetailFolderView.as_view()),
    path('api/v1/items/', ItemView.as_view()),
    path('api/v1/items/<int:pk>/', DetailItemView.as_view()),
]
