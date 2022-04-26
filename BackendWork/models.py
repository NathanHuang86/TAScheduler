from django.db import models
from multiselectfield import MultiSelectField
from _datetime import time


class MyUser(models.Model):
    ROLE_CHOICES = (('Teaching Assistant', 'TEACHING_ASSISTANT'), ('Instructor', 'INSTRUCTOR'), ('Admin', 'ADMIN'))
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='Teaching Assistant')

    def __str__(self):
        return self.username

    def getName(self):
        return self.name


class ClassList(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    SCHEDULE_CHOICES = (('Sunday', 'SUNDAY'), ('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'))
    SECTION_TYPE_CHOICES = (('Discussion', 'DISCUSSION'), ('Lab', 'LAB'))
    Class = models.ForeignKey(ClassList, on_delete=models.SET_NULL, null=True)
    TA = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    sectionNumber = models.IntegerField(default=0)
    sectionType = models.CharField(max_length=30, choices=SECTION_TYPE_CHOICES, default='Discussion')
    schedule = MultiSelectField(max_length=30, choices=SCHEDULE_CHOICES)
    startTime = models.TimeField(default=time(0, 0, 0))
    endTime = models.TimeField(default=time(0, 0, 0))
