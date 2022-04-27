from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


# Create your tests here.
class TestLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.save()

    def test_correctLogin(self):
        for i in self.thingList.keys():
            resp = self.client.post("", {"username": i, "password": i})
            print(self.client.get("username"))
            assert(resp.status_code == 200, "name not passed from Login to list")


class TestIncorrectLogin(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.save()

    def test_incorrectPassword(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.status_code != 200, "Test shouldn't pass due to incorrect username.")

    def test_incorrectUsername(self):
        for i in self.thingList.keys():
            resp = self.client.post("/", {"username": i, "password": i}, follow=True)
            self.assertFalse(resp.status_code != 200, "Test shouldn't pass due to incorrect password.")
