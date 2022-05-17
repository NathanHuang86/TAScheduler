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
        return render(request, "home.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                             'courses': MyUser.objects.get(
                                                 username=request.session["user"]).assignedClasses.all(),
                                             'sections': Section.objects.filter(
                                                 assignedUser=MyUser.objects.get(username=request.session["user"]))})

    def post(self, request):
        if request.POST.get("editUser"):
            return render(request, "home.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                                 'courses': MyUser.objects.get(
                                                     username=request.session["user"]).assignedClasses.all(),
                                                 'sections': Section.objects.filter(
                                                     assignedUser=MyUser.objects.get(
                                                         username=request.session["user"])),
                                                 'editing': "allowed"})

        elif request.POST.get("saveEditUser"):
            onFile = MyUser.objects.get(username=request.POST["saveEditUser"])

            if request.POST.get("username"):
                if len(MyUser.objects.filter(username=request.POST.get("username"))) != 0:
                    errorMessage = "Error: Username '" + request.POST.get("username") + "' is already in use."
                    return render(request, "home.html",
                                  {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                   'users': MyUser.objects.all(),
                                   'error': errorMessage})
                else:
                    onFile.username = request.POST.get("username")

            if request.POST.get("name"):
                onFile.name = request.POST.get("name")
            if request.POST.get("password"):
                onFile.password = request.POST.get("password")
            if request.POST.get("email"):
                onFile.email = request.POST.get("email")
            if request.POST.get("phone"):
                onFile.phone = request.POST.get("phone")
            onFile.save()
            request.session["user"] = onFile.username
            successMessage = "User '" + onFile.username + "' edited."

            return render(request, "home.html", {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                                 'courses': MyUser.objects.get(
                                                     username=request.session["user"]).assignedClasses.all(),
                                                 'sections': Section.objects.filter(
                                                     assignedUser=MyUser.objects.get(
                                                         username=request.session["user"])),
                                                 'success': successMessage})


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
                if len(MyUser.objects.filter(username=request.POST.get("username"))) != 0:
                    errorMessage = "Error: Username '" + request.POST.get("username") + "' is already in use."
                    return render(request, "users.html",
                                  {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                   'users': MyUser.objects.all(),
                                   'error': errorMessage})
                else:
                    onFile.username = request.POST.get("username")

            if request.POST.get("name"):
                onFile.name = request.POST.get("name")
            if request.POST.get("password"):
                onFile.password = request.POST.get("password")
            if request.POST.get("email"):
                onFile.email = request.POST.get("email")
            if request.POST.get("phone"):
                onFile.phone = request.POST.get("phone")
            if onFile.role != request.POST.get("role"):
                onFile.role = request.POST.get("role")
            onFile.save()
            successMessage = "User '" + onFile.username + "' edited."

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
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]), 'users': users})

        elif request.POST.get("deleteUser"):
            MyUser.objects.get(username=request.POST.get("deleteUser")).delete()
            successMessage = "User '" + request.POST.get("deleteUser") + "' deleted."
            return render(request, "users.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'users': MyUser.objects.all(),
                           'success': successMessage})
        elif request.POST.get("viewAssignments"):
            request.session["userAssignments"] = request.POST.get("viewAssignments")
            return redirect("userAssignments/")


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
            courseName = ClassList.objects.get(name=request.POST.get('deleteCourse')).name
            oldSections = Section.objects.filter(
                Class=ClassList.objects.get(name=request.POST.get('deleteCourse'))).delete()
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
            return render(request, "sections.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'sections': Section.objects.filter(
                               Class=ClassList.objects.get(name=request.session["thisCourse"])),
                           'startTime': Section.objects.get(
                               Class=ClassList.objects.get(name=request.session["thisCourse"]),
                               sectionNumber=request.session['thisSection']).startTime.strftime("%H:%M"),
                           'endTime': Section.objects.get(
                               Class=ClassList.objects.get(name=request.session["thisCourse"]),
                               sectionNumber=request.session['thisSection']).endTime.strftime("%H:%M"),
                           'editingSection': int(request.session.pop('thisSection')),
                           'courseUsers': MyUser.objects.filter(
                               assignedClasses=ClassList.objects.get(name=request.session["thisCourse"]))})

        successMessage = ""

        if request.POST.get('deleteSection'):
            sectionType = Section.objects.get(Class=ClassList.objects.get(name=request.session['thisCourse']),
                                              sectionNumber=request.POST.get('deleteSection')).sectionType
            Section.objects.get(Class=ClassList.objects.get(name=request.session['thisCourse']),
                                sectionNumber=request.POST.get('deleteSection')).delete()
            successMessage = sectionType + ' ' + request.POST.get('deleteSection') + ' deleted.'

        elif request.POST.get('saveSection'):
            onFile = Section.objects.get(Class=ClassList.objects.get(name=request.session['thisCourse']),
                                         sectionNumber=int(request.POST['saveSection']))

            if request.POST.get('sectionNumber'):
                try:
                    if len(Section.objects.filter(Class=ClassList.objects.get(name=request.session['thisCourse']),
                                                  sectionNumber=request.POST.get('sectionNumber'))) != 0:
                        errorMessage = "Section Number " + str(request.POST.get("sectionNumber")) + " already exists."
                        return render(request, "sections.html",
                                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                                       'sections': Section.objects.filter(
                                           Class=ClassList.objects.get(name=request.session["thisCourse"])),
                                       'error': errorMessage})
                    else:
                        onFile.sectionNumber = int(request.POST.get("sectionNumber"))

                except:
                    errorMessage = "Section Number must be an integer."
                    return render(request, "sections.html",
                                  {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                                   'course': ClassList.objects.get(name=request.session["thisCourse"]),
                                   'sections': Section.objects.filter(
                                       Class=ClassList.objects.get(name=request.session["thisCourse"])),
                                   "error": errorMessage})

            if request.POST.get("assignedUser"):
                onFile.assignedUser = MyUser.objects.get(username=request.POST.get("assignedUser"))
            else:
                onFile.assignedUser = None
            if request.POST.get("sectionType"):
                onFile.sectionType = request.POST.get("sectionType")
            if request.POST.get("monday"):
                onFile.monday = True
            else:
                onFile.monday = False
            if request.POST.get("tuesday"):
                onFile.tuesday = True
            else:
                onFile.tuesday = False
            if request.POST.get("wednesday"):
                onFile.wednesday = True
            else:
                onFile.wednesday = False
            if request.POST.get("thursday"):
                onFile.thursday = True
            else:
                onFile.thursday = False
            if request.POST.get("friday"):
                onFile.friday = True
            else:
                onFile.friday = False
            if request.POST.get("startTime"):
                onFile.startTime = request.POST.get("startTime")
            if request.POST.get("endTime"):
                onFile.endTime = request.POST.get("endTime")

            onFile.save()
            successMessage = "Section Number " + str(onFile.sectionNumber) + " edited."

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
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'success': successMessage})
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
                       'users': MyUser.objects.filter(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"]))})

    def post(self, request):
        try:
            int(request.POST["sectionNumber"])
        except:
            errorMessage = "Section Number must be an integer."
            return render(request, "createSection.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'users': MyUser.objects.filter(role='Teaching Assistant'),
                           'error': errorMessage})
        if len(Section.objects.filter(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                                      sectionNumber=request.POST.get('sectionNumber'))) != 0:
            errorMessage = 'Section number ' + request.POST.get('sectionNumber') + ' already exists.'
            return render(request, "createSection.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'users': MyUser.objects.filter(role='Teaching Assistant'),
                           'error': errorMessage})

        newSection = Section.objects.create(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                                            sectionNumber=request.POST["sectionNumber"],
                                            sectionType=request.POST["sectionType"])

        if request.POST.get('startTime'):
            newSection.startTime = request.POST['startTime']
        if request.POST.get('endTime'):
            newSection.endTime = request.POST['endTime']
        if request.POST.get('assignedUser'):
            newSection.assignedUser = MyUser.objects.get(username=request.POST["assignedUser"])
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
        if len(ClassList.objects.filter(name=request.POST["name"])) != 0:
            errorMessage = "Course '" + request.POST["name"] + "' already exists."
            return render(request, "createCourse.html",
                          {'instructors': MyUser.objects.filter(role='Instructor').values(),
                           'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'error': errorMessage})
        ClassList(name=request.POST["name"], term=request.POST["term"], year=request.POST["year"]).save()
        successMessage = "Course '" + request.POST["name"] + "' created."
        return render(request, "createCourse.html",
                      {'instructors': MyUser.objects.filter(role='Instructor').values(),
                       'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'success': successMessage})


class AssignedUsers(View):

    def get(self, request):
        try:
            request.session["user"]
        except:
            return redirect("/")
        return render(request, "assignedUsers.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'assignedUsers': MyUser.objects.filter(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                       'unassignedUsers': MyUser.objects.exclude(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"]))})

    def post(self, request):
        if request.POST.get('assignUser'):
            assignUser = MyUser.objects.get(username=request.POST.get('assignUser'))
            assignUser.assignedClasses.add(ClassList.objects.get(name=request.session["thisCourse"]))
            assignUser.save()
            successMessage = "Assigned '" + assignUser.username + "' to " + request.session["thisCourse"] + "."
            return render(request, "assignedUsers.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'assignedUsers': MyUser.objects.filter(
                               assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                           'unassignedUsers': MyUser.objects.exclude(
                               assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                           'success': successMessage})

        if request.POST.get('unassignUser'):
            assignUser = MyUser.objects.get(username=request.POST.get('unassignUser'))
            assignUser.assignedClasses.remove(ClassList.objects.get(name=request.session["thisCourse"]))
            sectionsWithAssignedUser = list(
                Section.objects.filter(Class=ClassList.objects.get(name=request.session["thisCourse"]),
                                       assignedUser=assignUser))
            for section in sectionsWithAssignedUser:
                section.assignedUser = None
                section.save()
            assignUser.save()
            successMessage = "Unassigned '" + assignUser.username + "' from " + request.session["thisCourse"] + "."
            return render(request, "assignedUsers.html",
                          {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                           'course': ClassList.objects.get(name=request.session["thisCourse"]),
                           'assignedUsers': MyUser.objects.filter(
                               assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                           'unassignedUsers': MyUser.objects.exclude(
                               assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                           'success': successMessage})

        errorMessage = "No user selected."
        return render(request, "assignedUsers.html",
                      {'sessionUser': MyUser.objects.get(username=request.session["user"]),
                       'course': ClassList.objects.get(name=request.session["thisCourse"]),
                       'assignedUsers': MyUser.objects.filter(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                       'unassignedUsers': MyUser.objects.exclude(
                           assignedClasses=ClassList.objects.get(name=request.session["thisCourse"])),
                       'error': errorMessage})


class UserAssignments(View):
    def get(self, request):
        return render(request, "userAssignments.html",
                      {'sessionUser': MyUser.objects.get(username=request.session['user']),
                       'viewingUser': MyUser.objects.get(username=request.session['userAssignments']),
                       'courses': MyUser.objects.get(username=request.session['userAssignments']).assignedClasses.all(),
                       'sections': Section.objects.filter(
                           assignedUser=MyUser.objects.get(username=request.session['userAssignments']))})
