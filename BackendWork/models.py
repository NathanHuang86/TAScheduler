from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)


class Class(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Permission(models.Model):
    API_Name = models.CharField
    label = models.CharField


class PermissionAssignment(models.Model):
    userID = models.ForeignKey(User)
    permissionAPIName = models.ForeignKey(Permission)


class Schedule(models.Model):
    sunday = models.BooleanField
    monday = models.BooleanField
    tuesday = models.BooleanField
    wednesday = models.BooleanField
    thursday = models.BooleanField
    friday = models.BooleanField
    saturday = models.BooleanField
    startTime = models.TimeField
    endTime = models.TimeField


class Section(models.Model):
    Class = models.ForeignKey(Class)
    TA = models.ForeignKey(User)
    schedule = models.ForeignKey(Schedule)
    time = models.TimeField
    sectionNumber = models.IntegerField
