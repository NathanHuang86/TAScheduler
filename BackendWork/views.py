from django.shortcuts import render, redirect
from django.views import View
from BackendWork.models import ClassList, MyUser, Section


# Create your views here.


class Landing(View):
    def post(self, request):
        if request.method == 'POST' and 'loginSubmit' in request.POST:
            Login.post(self, request)
        elif request.method == 'POST' and 'createAccountSubmit' in request.POST:
            CreateAccount.post(self, request)


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        noSuchUser = False
        badPassword = False

        try:
            m = MyUser.objects.get(username=request.POST['username'])
            noSuchUser = not (m.username == request.POST['username'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            print("No such user")
            return render(request, "login.html", {"message": "No such user exists."})
        elif badPassword:
            print("Bad password")
            return render(request, "login.html", {"message": "Password is incorrect."})
        else:
            request.session["role"] = m.role
            print(m.role)
            return redirect("home/")


class Home(View):

    def get(self, request):
        m = request.session["role"]
        return render(request, "home.html", {'sessionUser': m})


class CreateAccount(View):

    def get(self, request):
        m = request.session["role"]
        return render(request, "createAccount.html", {'sessionUser': m})

    def post(self, request):
        role = None
        if request.POST.get("button1") == "0":
            role = "Teaching Assistant"
        if request.POST.get("button1") == "1":
            role = "Instructor"
        if request.POST.get("button1") == "2":
            role = "Admin"

        newuser = MyUser(username=request.POST["username"], password=request.POST["password"],
                         name=request.POST["name"],
                         email=request.POST["email"], address=request.POST["address"], phone=request.POST["phone"],
                         role=role)

        for names in vars(newuser).values():
            print(names)
            if names == "":
                print("Didn't go through.")
                return render(request, "createAccount.html", {"message": "Invalid data entered"})

        m = request.session["role"]
        newuser.save()
        return render(request, "createAccount.html", {'sessionUser': m})


class CreateCourses(View):

    def get(self, request):
        instructors = MyUser.objects.filter(role='Instructor')
        m = request.session["role"]
        print(m)
        return render(request, "createCourses.html", {'instructors': instructors, 'sessionUser': m})

    def post(self, request):
        instructors = MyUser.objects.filter(role='Instructor').values()
        d = MyUser.objects.filter(name=request.POST["userSelect"])
        newcourse = ClassList(name=request.POST["name"], owner=d[0])

        m = request.session["role"]
        newcourse.save()
        return render(request, "createCourses.html", {'instructors': instructors, 'sessionUser': m})


class Users(View):

    def get(self, request):
        m = request.session["role"]
        users = MyUser.objects.all()
        return render(request, "list_of_users.html", {'sessionUser': m, 'users': users})


class Courses(View):

    def get(self, request):
        m = request.session["role"]
        courses = ClassList.objects.all()
        return render(request, "list_of_courses.html", {'sessionUser': m, 'courses': courses})

    def post(self, request):
        m = request.session["role"]
        thisCourseName = request.POST['thisCourse']
        print("ThisCourse =", request.POST['thisCourse'])
        thisCourse = ClassList.objects.get(name=thisCourseName)
        sections = Section.objects.filter(Class=thisCourse)
        return render(request, "list_of_sections.html", {'sessionUser': m, 'course': thisCourse, 'sections': sections})

class Sections(View):

    def get(self, request):
        m = request.session["role"]
        course = ClassList.objects.get(name='CS 251')
        sections = Section.objects.filter(Class=course)
        return render(request, "list_of_sections.html", {'sessionUser': m, 'course': course, 'sections': sections})


class EditUser(View):

    def get(self, request):
        m = request.session["role"]
        users = MyUser.objects.filter()
        return render(request, "list_of_users.html", {'sessionUser': m, 'users': users})

