from django.test import TestCase
from StuffTracker.models import Stuff, MyUser
from django.test import Client


class TestAddItem(TestCase):
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

    def test_AddItem(self):
        Stuff(name="Sauce", owner=MyUser(name="Mike", password="Mike")).save()
        resp = self.client.post("/", {"name": "Mike", "Owner": "Mike"}, follow=True)
        self.assertEqual(resp.context["things"], ["Bobble head", "Mike Tyson", "Sauce"], "Item should be added")

    def test_EmptyItem(self):
        Stuff(name="Sauce", owner=MyUser(name="Mike", password="Mike")).save()
        resp = self.client.post("/", {"name": "Mike", "Owner": "Mike"}, follow=True)
        self.assertEqual(resp.context["things"], ["Bobble head", "Mike Tyson"], "Item shouldn't be added")