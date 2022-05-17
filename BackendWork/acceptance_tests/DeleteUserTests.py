from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


# Create your tests here.
class TestAccountDelete(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.role = "Admin"
            temp.save()

    def test_DeleteAccount(self):
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("createAccount/", follow=True)
        self.client.post("/createAccount/", {"username": "alice", "password": "password", "name": "alice",
                                             "email": "alice@gmail.com", "address": "Bob", "phone": "Bob",
                                             "button1": "1"}, follow=True)
        alice = MyUser.objects.filter(username="alice")
        self.assertEqual(len(alice), 1)
        self.client.post("/users/", {"deleteUser": "alice"}, follow=True)
        alice = MyUser.objects.filter(username="alice")
        self.assertEqual(len(alice), 0)