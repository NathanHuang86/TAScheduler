from django.shortcuts import render, redirect
from django.views import View
from BackendWork.models import ClassList, MyUser


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
            request.session["username"] = m.name
            return redirect("/createAccount/")


class CreateAccount(View):
    def get(self, request):
        m = request.session["username"]
        return render(request, "createAccount.html", {"username": m})

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
        return render(request, "createAccount.html", {"message": "Invalid data entered"})


class CreateCourses(View):
    def get(self, request):
        instructors = MyUser.objects.filter(role='Instructor')
        m = request.session["username"]
        return render(request, "createCourses.html", {'instructors': instructors})

    def post(self, request):
        instructors = MyUser.objects.filter(role='Instructor').values()
        d = MyUser.objects.filter(name=request.POST["userSelect"])
        newcourse = ClassList(name=request.POST["name"], owner=d[0])
        newcourse.save()

        return render(request, "createCourses.html", {'instructors': instructors})

class Users(View):
    def get(self, request):
        users = MyUser.objects.filter()
        return render(request, "users.html", {'users': users})

    def post(self, request):
        pass