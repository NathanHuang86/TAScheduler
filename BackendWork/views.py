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


class Users(View):

    def get(self, request):
        m = request.session["role"]
        users = MyUser.objects.all()
        return render(request, "list_of_users.html", {'sessionUser': m, 'users': users})

    def post(self, request):
        thisUsername = request.POST['thisUser']
        request.session['thisUser'] = thisUsername
        return redirect("editUser/")


class Courses(View):

    def get(self, request):
        m = request.session["role"]
        courses = ClassList.objects.all()
        return render(request, "list_of_courses.html", {'sessionUser': m, 'courses': courses})

    def post(self, request):

        # print("thisCourseSections =", request.POST['thisCourseSections'])
        # print("thisCourseEdit =", request.POST['thisCourseEdit'])

        if request.POST.get('thisCourseSections'):
            thisCourseName = request.POST['thisCourseSections']
            thisCourse = ClassList.objects.get(name=thisCourseName)
            request.session["thisCourse"] = thisCourse.name
            return redirect("sections/")

        elif request.POST.get('thisCourseEdit'):
            thisCourseName = request.POST['thisCourseEdit']
            request.session["thisCourse"] = thisCourseName
            return redirect("editCourse/")


class Sections(View):

    def get(self, request):
        m = request.session["role"]
        thisCourseName = request.session["thisCourse"]
        thisCourse = ClassList.objects.get(name=thisCourseName)
        sections = Section.objects.filter(Class=thisCourse)
        return render(request, "list_of_sections.html", {'sessionUser': m, 'course': thisCourse, 'sections': sections})

    def post(self, request):
        m = request.session["role"]
        thisUsername = request.POST['thisUser']
        thisUser = MyUser.objects.get(username=thisUsername)
        return render(request, "editUser.html", {'sessionUser': m, 'thisUser': thisUser})


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


class CreateSection(View):

    def get(self, request):
        m = request.session["role"]
        thisCourseName = request.session["thisCourse"]
        thisCourse = ClassList.objects.get(name=thisCourseName)
        TAs = MyUser.objects.filter(role='Teaching Assistant')
        return render(request, "createSection.html", {'sessionUser': m, 'course': thisCourse, 'TAs': TAs})


class CreateCourses(View):

    def get(self, request):
        instructors = MyUser.objects.filter(role='Instructor')
        m = request.session["role"]
        return render(request, "createCourses.html", {'instructors': instructors, 'sessionUser': m})

    def post(self, request):
        instructors = MyUser.objects.filter(role='Instructor').values()
        d = MyUser.objects.filter(name=request.POST["userSelect"])
        newcourse = ClassList(name=request.POST["name"], owner=d[0])

        m = request.session["role"]
        newcourse.save()
        return render(request, "createCourses.html", {'instructors': instructors, 'sessionUser': m})


class EditUser(View):

    def get(self, request):
        m = request.session["role"]
        thisUserName = request.session["thisUser"]
        thisUser = MyUser.objects.get(username=thisUserName)
        return render(request, "editUser.html", {'sessionUser': m, 'thisUser': thisUser})


class EditSection(View):

    def get(self, request):
        m = request.session["role"]
        thisCourseName = request.session["thisCourse"]
        thisCourse = ClassList.objects.get(name=thisCourseName)
        thisSection = Section.objects.get(Class=thisCourse, sectionNumber=request.POST['thisSection'])
        return render(request, "editSection.html", {'sessionUser': m, 'section': thisSection})


class EditCourses(View):

    def get(self, request):
        m = request.session["role"]
        thisCourseName = request.session["thisCourse"]
        thisCourse = ClassList.objects.get(name=thisCourseName)
        return render(request, "editCourse.html", {'sessionUser': m, 'course': thisCourse})