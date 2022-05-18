from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


# Create your tests here.
class TestAccountCreate(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.role = "Admin"
            temp.save()

    def test_CreateAccount(self):
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("createAccount/", follow=True)
        self.client.post("/createAccount/", {"username": "alice", "password": "password", "name": "alice",
                                             "email": "alice@gmail.com", "address": "Bob", "phone": "Bob",
                                             "button1": "1"}, follow=True)
        alice = MyUser.objects.filter(username="alice")
        self.assertEqual(len(alice), 1)

    def test_UniqueAccount(self):
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("createAccount/", follow=True)
        self.client.post("/createAccount/", {"username": "alice", "password": "password", "name": "alice",
                                             "email": "alice@gmail.com", "address": "Bob", "phone": "Bob",
                                             "button1": "1"}, follow=True)
        self.client.post("/createAccount/", {"username": "alice", "password": "password", "name": "alice",
                                             "email": "alice@gmail.com", "address": "Bob", "phone": "Bob",
                                             "button1": "1"}, follow=True)
        alice = MyUser.objects.filter(username="alice")
        self.assertEqual(len(alice), 1)


class TestFailAccount(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.role = "Admin"
            temp.save()

    def test_EmptyFields(self):
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("createAccount/", follow=True)
        self.client.post("/createAccount/", {"username": "", "password": "password", "name": "alice",
                                             "email": "alice@gmail.com", "address": "Bob", "phone": "Bob",
                                             "button1": "1"}, follow=True)
        alice = MyUser.objects.filter(username="alice")
        self.assertEqual(len(alice), 0)