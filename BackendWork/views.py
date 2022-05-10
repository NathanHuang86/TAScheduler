from django.contrib import auth
from django.shortcuts import render, redirect
from django.views import View

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
            return render(request, "login.html", {"message": "No such user exists."})
        elif badPassword:
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
        # checking the user
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
            request.session["thisCourse"] = request.POST['thisCourseSections']
            return redirect("sections/")

        elif request.POST.get('assignedUser'):
            request.session["thisCourse"] = request.POST['assignedUser']
            return redirect("assignedUsers/")

        elif request.POST.get('deleteCourse'):
            # TODO should delete sections on the course as well
            courseName = ClassList.objects.get(name=request.POST.get('deleteCourse')).name
            ClassList.objects.get(name=request.POST.get('deleteCourse')).delete()
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
        if request.POST.get('editSection'):
            request.session["thisSection"] = request.POST['editSection']
            print("Editing Section: " + request.session["thisSection"])
            return render(request, "sections.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'sections': Section.objects.filter(
                               Class=ClassList.objects.get(name=request.session["thisCourse"])),
                           'editingSection': request.session.pop('thisSection')})

        if request.POST.get('deleteSection'):
            sectionType = Section.objects.get(sectionNumber=request.POST.get('deleteSection')).sectionType
            Section.objects.get(sectionNumber=request.POST.get('deleteSection')).delete()
            successMessage = sectionType + ' ' + request.POST.get('deleteSection') + ' deleted.'
            return render(request, "sections.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'sections': Section.objects.filter(
                               Class=ClassList.objects.get(name=request.session["thisCourse"])),
                           'success': successMessage})

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

    def post(self, request):
        if len(Section.objects.filter(sectionNumber=request.POST.get('sectionNumber'))) != 0:
            errorMessage = 'Section number ' + request.POST.get('sectionNumber') + ' already exists.'
            return render(request, "createSection.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'users': MyUser.objects.filter(role='Teaching Assistant'),
                           'success': errorMessage})

        newSection = Section.objects.create(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                               assignedUser=MyUser.objects.get(username=request.POST["assignedUser"]),
                               sectionNumber=request.POST["sectionNumber"], sectionType=request.POST["sectionType"],
                               startTime=request.POST["startTime"], endTime=request.POST["endTime"])

        if request.POST.get('Monday'):
            newSection.monday = True
        if request.POST.get('Tuesday'):
            newSection.tuesday = True
        if request.POST.get('Wednesday'):
            newSection.wednesday = True
        if request.POST.get('Thursday'):
            newSection.thursday = True
        if request.POST.get('Friday'):
            newSection.friday = True

        newSection.save()

        successMessage = request.POST['sectionType'] + ' ' + request.POST[
            'sectionNumber'] + ' created for Class ' + ClassList.objects.get(
            name=request.session["thisCourse"]).name + "."
        return render(request, "createSection.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'users': MyUser.objects.filter(role='Teaching Assistant'),
                       'success': successMessage})


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
                       'users': MyUser.objects.filter(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"]))})
