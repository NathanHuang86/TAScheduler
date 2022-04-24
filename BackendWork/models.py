from django.db import models


class MyUser(models.Model):
    ROLE_CHOICES = (('Teaching Assistant', 'TEACHING_ASSISTANT'), ('Instructor', 'INSTRUCTOR'), ('Admin', 'ADMIN'))
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)
    role = models.CharField(choices=ROLE_CHOICES)


class ClassList(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)

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
    SECTION_TYPE_CHOICES = (('Discussion', 'DISCUSSION'), ('Lab', 'LAB'))
    Class = models.ForeignKey(ClassList, on_delete=models.SET_NULL, null=False)
    TA = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=False)
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=False)
    time = models.TimeField
    sectionNumber = models.IntegerField
    sectionType = models.CharField(choices=SECTION_TYPE_CHOICES)