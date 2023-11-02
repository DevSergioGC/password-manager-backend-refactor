from django.db import models
from django.contrib.auth.models import User
from folders import Folder


class Items(models.Model):
    id_item = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=300)

    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    folder = models.ForeignKey(
        Folders, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_id(self):
        return self.id_item

    def get_name(self):
        return self.name

    def get_user(self):
        return self.user

    def get_folder(self):
        return self.folder

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_url(self):
        return self.url

    def get_description(self):
        return self.description
