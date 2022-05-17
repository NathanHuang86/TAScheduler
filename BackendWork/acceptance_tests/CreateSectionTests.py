from django.test import TestCase
from BackendWork.models import ClassList, MyUser, Section
from django.test import Client

class TestSectionCreate(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.math = ClassList.objects.create(name='math', term='Fall', year=2022)
        self.Mike = MyUser.objects.create(username='Mike', password='Mike', name='Mike',
                                             email='mike@yahoo.com', address='sometown', phone='123-456-7892',
                                             role='Admin')
    def test_CreateSection(self):
        mathSections = Section.objects.filter(Class=self.math)
        self.assertEqual(len(mathSections), 0)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {'thisCourseSections': "math"})
        self.client.post("/createSection/", {"sectionNumber": "101", "sectionType": "Lecture"}, follow=True)
        mathClasses = ClassList.objects.filter(name=self.math)
        self.assertEqual(len(mathClasses), 1)

    def test_CreateUniqueSectionNumber(self):
        mathSections = Section.objects.filter(Class=self.math)
        self.assertEqual(len(mathSections), 0)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {'thisCourseSections': "math"})
        self.client.post("/createSection/", {"sectionNumber": "101", "sectionType": "Lecture"}, follow=True)
        mathClasses = ClassList.objects.filter(name=self.math)
        self.assertEqual(len(mathClasses), 1)
        self.client.post("/createSection/", {"sectionNumber": "101", "sectionType": "Lecture"}, follow=True)
        mathClasses = ClassList.objects.filter(name=self.math)
        self.assertEqual(len(mathClasses), 1)