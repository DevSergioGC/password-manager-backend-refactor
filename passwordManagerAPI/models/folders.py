from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    id_folder = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=False, blank=False, related_name='folders')

    def __str__(self):
        return self.name
