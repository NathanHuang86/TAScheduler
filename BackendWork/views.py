from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from BackendWork.models import ClassList, MyUser, Section


# Create your views here.

class Login(View):
    def get(self, request):
        auth.logout(request)
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
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "home.html", {'sessionUser': MyUser.objects.get(username=request.session["user"])})


class Users(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "users.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                              'users': MyUser.objects.all()})

    def post(self, request):
        if request.POST.get('saveEditUser'):
            onFile = MyUser.objects.get(username=request.POST['saveEditUser'])
            if request.POST.get("username"):
                if len(MyUser.objects.filter(username=request.POST.get("username"))) == 0:
                    onFile.username = request.POST.get("username")
                else:
                    errorMessage = "Error: Username '" + request.POST.get("username") + "' is already in use."
                    return render(request, "users.html",
                                  {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                   'users': MyUser.objects.all(),
                                   'error': errorMessage})
            madeChange = False
            successMessage = ""
            if request.POST.get("name"):
                onFile.name = request.POST.get("name")
                madeChange = True
            if request.POST.get("password"):
                onFile.password = request.POST.get("password")
                madeChange = True
            if request.POST.get("email"):
                onFile.email = request.POST.get("email")
                madeChange = True
            if request.POST.get("phone"):
                onFile.phone = request.POST.get("phone")
                madeChange = True
            if onFile.role != request.POST.get("role"):
                onFile.role = request.POST.get("role")
                madeChange = True
            onFile.save()
            if madeChange:
                successMessage = "User '" + request.POST.get("saveEditUser") + "' edited."
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'users': MyUser.objects.all(),
                           'success': successMessage})

        elif request.POST.get('editUser'):
            request.session["userEdit"] = request.POST['editUser']
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'users': MyUser.objects.all(),
                           'editingUser': request.session.pop('userEdit')})

        elif request.POST.get('cancelEdit'):
            users = MyUser.objects.all()
            return render(request, "users.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]), 'users': users})

        elif request.POST.get("deleteUser"):
            MyUser.objects.get(username=request.POST.get("deleteUser")).delete()
            successMessage = "User '" + request.POST.get("deleteUser") + "' deleted."
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'users': MyUser.objects.all(),
                           'success': successMessage})

class Courses(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "courses.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'courses': ClassList.objects.all()})

    def post(self, request):
        if request.POST.get('thisCourseSections'):
            thisCourseName = request.POST['thisCourseSections']
            thisCourse = ClassList.objects.get(name=thisCourseName)
            request.session["thisCourse"] = thisCourse.name
            return redirect("sections/")

        elif request.POST.get('assignedUser'):
            thisCourseName = request.POST['assignedUser']
            request.session["thisCourse"] = thisCourseName
            return redirect("assignedUsers/")

        elif request.POST.get('deleteCourse'):
            courseName = ClassList.objects.get(id=request.POST.get('deleteCourse')).name
            ClassList.objects.get(id=request.POST.get('deleteCourse')).delete()
            successMessage = "Course '" + courseName + "' deleted."
            return render(request, "courses.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'courses': ClassList.objects.all(),
                           'success': successMessage})


class Sections(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "sections.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'sections': Section.objects.filter(
                           Class=ClassList.objects.get(name=request.session["thisCourse"]))})

    def post(self, request):
        request.session['thisSection'] = request.POST['thisSection']
        return redirect("editSection/")


class CreateAccount(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "createAccount.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"])})

    def post(self, request):
        role = None
        if request.POST.get("button1") == "0":
            role = "Teaching Assistant"
        if request.POST.get("button1") == "1":
            role = "Instructor"
        if request.POST.get("button1") == "2":
            role = "Admin"

        if len(MyUser.objects.filter(username=request.POST["username"])) == 0:
            newuser = MyUser(username=request.POST["username"], password=request.POST["password"],
                         name=request.POST["name"],
                         email=request.POST["email"], address=request.POST["address"], phone=request.POST["phone"],
                         role=role)
            newuser.save()
            successMessage = "Account '" + request.POST["username"] + "' created."
            return render(request, "createAccount.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]), 'success': successMessage})
        else:
            errorMessage = "Error: Username '" + request.POST["username"] + "' is already in use."
            return render(request, "createAccount.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]), 'error': errorMessage})


class CreateSection(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "createSection.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'users': MyUser.objects.filter(role='Teaching Assistant')})


class CreateCourses(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "createCourse.html",
                      {'instructors': MyUser.objects.filter(role='Instructor'),
                       'sessionUser': MyUser.objects.get(username=request.session["user"])})

    def post(self, request):
        ClassList(name=request.POST["name"], term=request.POST["term"], year=request.POST["year"]).save()
        successMessage = "Course '" + request.POST["name"] + "' created."
        return render(request, "createCourse.html",
                      {'instructors': MyUser.objects.filter(role='Instructor').values(),
                       'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'success': successMessage})


class EditUser(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "editUser.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'thisUser': MyUser.objects.get(username=request.session["thisUser"])})


class EditSection(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "editSection.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'section': Section.objects.get(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                                                      sectionNumber=request.session['thisSection'])})


class AssignedUsers(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "assignedUsers.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'users': MyUser.objects.filter(assignedClasses=ClassList.objects.get(name=request.session["thisCourse"]))})