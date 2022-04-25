from django.db import models


class MyUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ClassList(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    API_Name = models.CharField
    label = models.CharField

    def __str__(self):
        return self.name


class PermissionAssignment(models.Model):
    userID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    permissionAPIName = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


class Section(models.Model):
    Class = models.ForeignKey(ClassList, on_delete=models.CASCADE)
    TA = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    time = models.TimeField
    sectionNumber = models.IntegerField

    def __str__(self):
        return self.name
