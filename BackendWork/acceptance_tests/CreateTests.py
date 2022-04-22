from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


# Create your tests here.
class TestAccountCreate(TestCase):
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

    def test_CreateAccount(self):
        ClassList(username="Sauce", owner=MyUser(username='Tys', password="Tys")).save()
        resp = self.client.post("/", {"username": "Tys", "password": "Tys"}, follow=True)
        self.assertEqual(resp.context["username"], "Tys", "name not passed from Login to list")
        self.assertEqual(resp.context["password"], "Tys", "name not passed from Login to list")


class TestFailAccount(TestCase):
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

    def test_EmptyFields(self):
        ClassList(username="Sauce", owner=MyUser(username="Chic", password=None)).save()
        resp = self.client.post("/", {"username": "Chic", "password": None}, follow=True)
        self.assertEqual(resp.context["password"], None, "Should be passing")

    def test_EmptyUser(self):
        ClassList(username="Sauce", owner=MyUser(username=None, password="Chic")).save()
        with self.assertRaises(KeyError, "Key shouldn't pass through"):
            resp = self.client.post("/", {"username": None, "password": "Link"}, follow=True)
