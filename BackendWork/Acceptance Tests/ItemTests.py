from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


class TestAddItem(TestCase):
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

    def test_AddItem(self):
        ClassList(username="Sauce", owner=MyUser(username="Mike", password="Mike")).save()
        resp = self.client.post("/", {"username": "Mike", "Owner": "Mike"}, follow=True)
        self.assertEqual(resp.context["things"], ["Bobble head", "Mike Tyson", "Sauce"], "Item should be added")

    def test_EmptyItem(self):
        ClassList(username="Sauce", owner=MyUser(username="Mike", password="Mike")).save()
        resp = self.client.post("/", {"username": "Mike", "Owner": "Mike"}, follow=True)
        self.assertEqual(resp.context["things"], ["Bobble head", "Mike Tyson"], "Item shouldn't be added")
