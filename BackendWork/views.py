from django.shortcuts import render, redirect
from django.views import View
from models import ClassList, MyUser


# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = MyUser.objects.get(name=request.POST['username'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser:
            return render(request, "login.html", {"message": "No such user exists."})
        elif badPassword:
            return render(request, "login.html", {"message": "Password is incorrect."})
        else:
            request.session["username"] = m.name
            return redirect("/createAccount/")


class Things(View):
    def get(self, request):
        m = request.session["username"]
        things = list(map(str, ClassList.objects.filter(owner__name=m)))
        return render(request, "things.html", {"name": m, "things": things})

    def post(self, request):
        m = request.session["name"]
        s = request.POST.get('stuff', '')
        if s != '':
            newThing = ClassList(name=s, owner=MyUser.objects.get(name=m))
            newThing.save()
        things = list(map(str, ClassList.objects.filter(owner__name=m)))
        return render(request, "things.html", {"username": m, "things": things})
