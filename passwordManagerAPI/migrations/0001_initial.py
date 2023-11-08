# Generated by Django 4.2.7 on 2023-11-08 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id_folder', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=300)),
                ('folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='passwordManagerAPI.folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
