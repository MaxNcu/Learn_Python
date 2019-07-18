from django.db import models

# Create your models here.

class News_Data(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=8)
    title = models.CharField(max_length=30)
    content = models.TextField(unique=True)
    datetime = models.DateTimeField(auto_now=True)

class User(models.Model):
    username = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=16)
