from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    id_folder = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def get_id(self):
        return self.id_folder
    
    def get_name(self):
        return self.name

    def get_user(self):
        return self.user