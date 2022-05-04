from django.contrib import admin
from .models import ClassList, MyUser, Section
# Register your models here.
admin.site.register(ClassList)
admin.site.register(MyUser)
admin.site.register(Section)
