from django.db import models
from _datetime import time


class ClassList(models.Model):
    TERM_CHOICES = (('Summer', 'SUMMER'), ('Fall', 'FALL'), ('Winter', 'WINTER'), ('Spring', 'SPRING'))
    name = models.CharField(max_length=20, unique=True)
    term = models.CharField(max_length=30, choices=TERM_CHOICES, default='Fall')
    year = models.IntegerField(default=2022)

    def __str__(self):
        return self.name


class MyUser(models.Model):
    ROLE_CHOICES = (('Teaching Assistant', 'TEACHING_ASSISTANT'), ('Instructor', 'INSTRUCTOR'), ('Admin', 'ADMIN'))
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    address = models.CharField(max_length=72)
    phone = models.CharField(max_length=10)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='Teaching Assistant')
    assignedClasses = models.ManyToManyField(ClassList, null=True, blank=True)

    def __str__(self):
        return self.username

    def getName(self):
        return self.name


class Section(models.Model):
    SCHEDULE_CHOICES = (('Sunday', 'SUNDAY'), ('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'))
    SECTION_TYPE_CHOICES = (('Discussion', 'DISCUSSION'), ('Lab', 'LAB'), ('Lecture', 'LECTURE'))
    Class = models.ForeignKey(ClassList, on_delete=models.SET_NULL, null=True)
    assignedUser = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True)
    sectionNumber = models.IntegerField(default=0)
    sectionType = models.CharField(max_length=30, choices=SECTION_TYPE_CHOICES, default='Discussion')
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    startTime = models.TimeField(default=time(0,0,0))
    endTime = models.TimeField(default=time(0,0,0))

    def __str__(self):
        return self.Class.name + " " + self.sectionType + " " + str(self.sectionNumber)