from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


class TestAddItem(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()

        self.thingList = {"Mike": "Mike", "Bob": "Bob"}

        for i in self.thingList.keys():
            temp = MyUser(username=i, password=i)
            temp.role = "Admin"
            temp.save()

        alice = MyUser(username='alice', password='password', name='alice',
                       email='alice@yahoo.com', address='somewhere', phone='123-456-7890',
                       role='Instructor')
        alice.save()

    def test_DeleteItem(self):
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("courses/", follow=True)
        self.client.post("createCourses/", follow=True)
        self.client.post("/createCourses/", {"name": "Bob", "term": "summer", "year": "2032"}, follow=True)
        Bob = ClassList.objects.filter(name="Bob")
        self.assertEqual(len(Bob), 1)
        self.client.post("courses/", follow=True)
        self.client.post("courses/", "deleteUser", {"name": "Bob"}, follow=True)
        self.assertEqual(len(Bob), 0)
