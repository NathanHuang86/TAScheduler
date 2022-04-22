from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)


class ClassList(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
