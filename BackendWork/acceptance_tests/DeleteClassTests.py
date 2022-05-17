from django.test import TestCase
from BackendWork.models import ClassList, MyUser
from django.test import Client


class TestClassDelete(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.math = ClassList.objects.create(name='math', term='Fall', year=2022)
        self.history = ClassList.objects.create(name='history', term='Winter', year=2022)
        self.science = ClassList.objects.create(name='science', term='Spring', year=2023)
        self.english = ClassList.objects.create(name='english', term='Summer', year=2023)
        self.Mike = MyUser.objects.create(username='Mike', password='Mike', name='Mike',
                                             email='mike@yahoo.com', address='sometown', phone='123-456-7892',
                                             role='Admin')
    def test_DeleteClass(self):
        mathClasses = ClassList.objects.filter(name="math")
        self.assertEqual(len(mathClasses), 1)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {"deleteCourse": "math"}, follow=True)
        mathClasses = ClassList.objects.filter(name="math")
        self.assertEqual(len(mathClasses), 0)