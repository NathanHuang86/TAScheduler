from django.test import TestCase
from StuffTracker.models import Stuff, MyUser
from django.test import Client


# Create your tests here.
class TestAccountCreate(TestCase):
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

    def test_CreateAccount(self):
        Stuff(name="Sauce", owner=MyUser(name='Tys', password="Tys")).save()
        resp = self.client.post("/", {"name": "Tys", "password": "Tys"}, follow=True)
        self.assertEqual(resp.context["name"], "Tys", "name not passed from login to list")
        self.assertEqual(resp.context["password"], "Tys", "name not passed from login to list")


class TestFailAccount(TestCase):
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

    def test_EmptyFields(self):
        Stuff(name="Sauce", owner=MyUser(name="Chic", password=None)).save()
        resp = self.client.post("/", {"name": "Chic", "password": None}, follow=True)
        self.assertEqual(resp.context["password"], None, "Should be passing")

    def test_EmptyUser(self):
        Stuff(name="Sauce", owner=MyUser(name=None, password="Chic")).save()
        with self.assertRaises(KeyError, "Key shouldn't pass through"):
            resp = self.client.post("/", {"name": None, "password": "Link"}, follow=True)
