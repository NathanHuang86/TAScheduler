from django.contrib import admin
from .models import ClassList, MyUser, Schedule, Section
# Register your models here.
admin.site.register(ClassList)
admin.site.register(MyUser)
admin.site.register(Schedule)
admin.site.register(Section)
