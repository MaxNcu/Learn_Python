# coding:utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
class User(models.Model):
    username = models.CharField(max_length=8,unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(unique=True)

class Datas(models.Model):
    uid = models.ForeignKey('Tasks',on_delete=models.CASCADE)
    # url = models.URLField()
    title = models.CharField(max_length=100)
    power = models.CharField(max_length=20)
    ip = models.GenericIPAddressField()
    open_port = RichTextUploadingField()
    date = models.DateTimeField(auto_now=True)

