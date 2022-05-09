from django.shortcuts import render, redirect
from django.views import View

from BackendWork.models import ClassList, MyUser, Section


# Create your views here.

class Login(View):
    def get(self, request):
        if request.session.get("user"):
            print("Popped User: " + request.session.pop("user"))
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
            request.session["user"] = m.username
            return redirect("home/")


class Home(View):

    def get(self, request):
        return render(request, "home.html", {'role': MyUser.objects.get(username=request.session["user"]).role})


class Users(View):

    def get(self, request):
        if not request.session.get("user"):
            return render(request, "login.html", {})
        return render(request, "users.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                                              'users': MyUser.objects.all()})

    def post(self, request):
        if request.POST.get('editUser'):
            request.session["userEdit"] = request.POST['editUser']
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                           'users': MyUser.objects.all(),
                           'editingUser': request.session.pop('userEdit')})

        elif request.POST.get('cancelEdit'):
            m = request.session["role"]
            users = MyUser.objects.all()
            print("cancel Edit here")
            return render(request, "users.html", {'sessionUser': m, 'users': users})

        elif request.POST.get('saveUser'):
            onFile = MyUser.objects.get(username=request.POST['saveUser'])
            print(onFile.username)

            if request.POST.get("username"):
                onFile.username = request.POST.get("username")
            if request.POST.get("name"):
                onFile.name = request.POST.get("name")
            if request.POST.get("password"):
                onFile.password = request.POST.get("password")
            if request.POST.get("email"):
                onFile.email = request.POST.get("email")
            if request.POST.get("phone"):
                onFile.phone = request.POST.get("phone")
            if request.POST.get("role"):
                onFile.role = request.POST.get("role")
            onFile.save()
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                           'users': MyUser.objects.all()})


class Courses(View):

    def get(self, request):
        m = request.session["role"]
        return render(request, "courses.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'courses': ClassList.objects.all()})

    def post(self, request):

        # print("thisCourseSections =", request.POST['thisCourseSections'])
        # print("thisCourseEdit =", request.POST['thisCourseEdit'])

        if request.POST.get('thisCourseSections'):
            thisCourseName = request.POST['thisCourseSections']
            thisCourse = ClassList.objects.get(name=thisCourseName)
            request.session["thisCourse"] = thisCourse.name
            return redirect("sections/")

        elif request.POST.get('assignedUser'):
            thisCourseName = request.POST['assignedUser']
            request.session["thisCourse"] = thisCourseName
            return redirect("assignedUsers/")


class Sections(View):

    def get(self, request):
        return render(request, "sections.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'sections': Section.objects.filter(
                           Class=ClassList.objects.get(name=request.session["thisCourse"]))})

    def post(self, request):
        request.session['thisSection'] = request.POST['thisSection']
        return redirect("editSection/")


class CreateAccount(View):

    def get(self, request):
        return render(request, "createAccount.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role})

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

        newuser.save()
        return render(request, "createAccount.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role})


class CreateSection(View):

    def get(self, request):
        return render(request, "createSection.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'users': MyUser.objects.filter(role='Teaching Assistant')})


class CreateCourses(View):

    def get(self, request):
        return render(request, "createCourse.html",
                      {'instructors': MyUser.objects.filter(role='Instructor'),
                       'sessionUser': MyUser.objects.get(username=request.session["user"]).role})

    def post(self, request):
        d = MyUser.objects.filter(name=request.POST["userSelect"])
        newcourse = ClassList(name=request.POST["name"], owner=d[0])
        newcourse.save()

        return render(request, "createCourse.html",
                      {'instructors': MyUser.objects.filter(role='Instructor').values(),
                       'sessionUser': MyUser.objects.get(username=request.session["user"]).role})


class EditUser(View):

    def get(self, request):
        return render(request, "editUser.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'thisUser': MyUser.objects.get(username=request.session["thisUser"])})


class EditSection(View):

    def get(self, request):
        return render(request, "editSection.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'section': Section.objects.get(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                                                      sectionNumber=request.session['thisSection'])})


class AssignedUsers(View):

    def get(self, request):
        return render(request, "assignedUsers.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]).role,
                       'course': ClassList.objects.get(name=request.session["thisCourse"])})
