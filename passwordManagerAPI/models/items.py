from django.db import models
from django.contrib.auth.models import User
from .folders import Folder


class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=300)

    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folder, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
