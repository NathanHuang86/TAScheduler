from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


# Create your tests here.
class TestLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": {"Bobble head", "Mike Tyson"}, "Bob": {"Crackers", "Digimon"}}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                ClassList(username=j, owner=temp).save()

    def test_correctName(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"username": i, "password": i}, follow=True)
            self.assertEqual(resp.context["username"], i, "name not passed from Login to list")


class TestIncorrectLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": {"Bobble head", "Mike Tyson"}, "Bob": {"Crackers", "Digimon"}}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                ClassList(username=j, owner=temp).save()

    def test_incorrectPassword(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.context["password"], "Bubby Kot", "Password shouldn't pass")

    def test_incorrectUsername(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.context["username"], "Bubby Kot", "Username doesn't exist")
