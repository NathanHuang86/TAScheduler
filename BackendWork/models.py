from django.db import models
from multiselectfield import MultiSelectField


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
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)


class Section(models.Model):
    SCHEDULE_CHOICES = (('Sunday', 'SUNDAY'), ('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'))
    SECTION_TYPE_CHOICES = (('Discussion', 'DISCUSSION'), ('Lab', 'LAB'))
    Class = models.ForeignKey(ClassList, on_delete=models.SET_NULL, null=False)
    TA = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=False)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    sectionNumber = models.IntegerField
    sectionType = models.CharField(choices=SECTION_TYPE_CHOICES)
    schedule = MultiSelectField(choices=SCHEDULE_CHOICES)
    startTime = models.TimeField
    endTime = models.TimeField