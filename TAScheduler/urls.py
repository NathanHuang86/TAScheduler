"""TAScheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BackendWork.views import Login, Home, Users, Courses, Sections, CreateAccount, CreateCourses, CreateSection, UserAssignments, AssignedUsers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Login.as_view()),
    path("home/", Home.as_view()),
    path("users/", Users.as_view()),
    path("courses/", Courses.as_view()),
    path("courses/sections/", Sections.as_view()),
    path("createAccount/", CreateAccount.as_view()),
    path("createCourses/", CreateCourses.as_view()),
    path("courses/createSection/", CreateSection.as_view()),
    path("users/userAssignments/", UserAssignments.as_view()),
    path("courses/assignedUsers/", AssignedUsers.as_view())
]
