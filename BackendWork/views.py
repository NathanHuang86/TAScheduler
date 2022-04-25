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
        newuser = MyUser(username=request.POST["username"], password=request.POST["password"],
                         name=request.POST["name"],
                         email=request.POST["email"], address=request.POST["address"], phone=request.POST["phone"])

        if request.POST["username"] == "" or request.POST["password"] == "" or request.POST["name"] == "" or request.POST["email"] == "" or request.POST["address"] == "" or request.POST["phone"] == "":
            return render(request, "createAccount.html", {"message": "Invalid data entered"})

        newuser.save()
        return render(request, "createAccount.html", {"message": "Invalid data entered"})


class Courses(View):
    def get(self, request):
        instructors = MyUser.objects.filter(role='Instructor')
        m = request.session["username"]
        return render(request, "courses.html", {'instructors': instructors})

    def post(self, request):
        instructors = MyUser.objects.filter(role='Instructor').values().name
        newcourse = ClassList(name=request.POST["name"], owner=request.POST["owner"])
        newcourse.save()
        print(instructors)
        return render(request, "courses.html", {'instructors': instructors})
