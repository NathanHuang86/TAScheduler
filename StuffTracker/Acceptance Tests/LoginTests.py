from django.test import TestCase
from StuffTracker.models import Stuff, MyUser
from django.test import Client


# Create your tests here.
class TestLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": {"Bobble head", "Mike Tyson"}, "Bob": {"Crackers", "Digimon"}}

        for i in self.thingList.keys():
            temp = MyUser(name=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j, owner=temp).save()

    def test_correctName(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"name": i, "password": i}, follow=True)
            self.assertEqual(resp.context["name"], i, "name not passed from login to list")


class TestIncorrectLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": {"Bobble head", "Mike Tyson"}, "Bob": {"Crackers", "Digimon"}}

        for i in self.thingList.keys():
            temp = MyUser(name=i, password=i)
            temp.save()
            for j in self.thingList[i]:
                Stuff(name=j, owner=temp).save()

    def test_incorrectPassword(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"name": i, "password": i}, follow=True)
            self.assertFalse(resp.context["password"], "Bubby Kot", "Password shouldn't pass")

    def test_incorrectUsername(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"name": i, "password": i}, follow=True)
            self.assertFalse(resp.context["name"], "Bubby Kot", "Username doesn't exist")
