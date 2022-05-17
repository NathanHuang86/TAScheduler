from django.test import TestCase
from BackendWork.models import ClassList, MyUser, Section
from django.test import Client
from _datetime import time

class TestSectionEdit(TestCase):
    client = None
    theList = None

    def setUp(self):
        self.client = Client()
        self.Mike = MyUser.objects.create(username='Mike', password='Mike', name='Mike',
                                          email='mike@yahoo.com', address='sometown', phone='123-456-7892',
                                          role='Admin')
        self.alice = MyUser.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com',
                                           address='somewhere', phone='123-456-7890', role='Teaching Assistant')
        self.bob = MyUser.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com',
                                         address='someplace', phone='123-456-7891', role='Teaching Assistant')
        self.charlie = MyUser.objects.create(username='charlie', password='123password', name='charlie',
                                             email='charlie@yahoo.com', address='sometown', phone='123-456-7892',
                                             role='Teaching Assistant')
        self.theProfessor = MyUser.objects.create(username='professor', password='badpassword', name='professor',
                                                  email='professor@yahoo.com', address='uwmcampus',
                                                  phone='123-456-7893', role='Instructor')
        self.math = ClassList.objects.create(name='math', term='Fall', year=2022)
        self.history = ClassList.objects.create(name='history', term='Winter', year=2022)
        self.science = ClassList.objects.create(name='science', term='Spring', year=2023)
        self.english = ClassList.objects.create(name='english', term='Summer', year=2023)
        self.mathDiscussionSection1 = Section.objects.create(Class=self.math, assignedUser=self.alice, sectionNumber=1,
                                                             sectionType='Discussion', monday=True, tuesday=False,
                                                             wednesday=True, thursday=False, friday=False,
                                                             startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.mathDiscussionSection2 = Section.objects.create(Class=self.math, assignedUser=self.bob, sectionNumber=2,
                                                             sectionType='Discussion', monday=True, tuesday=False,
                                                             wednesday=True, thursday=False, friday=False,
                                                             startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.mathLabSection1 = Section.objects.create(Class=self.math, assignedUser=self.charlie, sectionNumber=3,
                                                      sectionType='Lab', monday=False, tuesday=True, wednesday=False,
                                                      thursday=False, friday=False, startTime=time(13, 0, 0),
                                                      endTime=time(14, 30, 0))
        self.mathLabSection2 = Section.objects.create(Class=self.math, assignedUser=self.charlie, sectionNumber=4,
                                                      sectionType='Lab', monday=False, tuesday=False, wednesday=True,
                                                      thursday=False, friday=False, startTime=time(13, 0, 0),
                                                      endTime=time(14, 30, 0))
        self.historyDiscussionSection1 = Section.objects.create(Class=self.history, assignedUser=self.alice,
                                                                sectionNumber=1, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.historyDiscussionSection2 = Section.objects.create(Class=self.history, assignedUser=self.bob,
                                                                sectionNumber=2, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.historyLabSection1 = Section.objects.create(Class=self.history, assignedUser=self.charlie, sectionNumber=3,
                                                         sectionType='Lab', monday=False, tuesday=True, wednesday=False,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
        self.historyLabSection2 = Section.objects.create(Class=self.history, assignedUser=self.charlie, sectionNumber=4,
                                                         sectionType='Lab', monday=False, tuesday=False, wednesday=True,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
        self.scienceDiscussionSection1 = Section.objects.create(Class=self.science, assignedUser=self.alice,
                                                                sectionNumber=1, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.scienceDiscussionSection2 = Section.objects.create(Class=self.science, assignedUser=self.bob,
                                                                sectionNumber=2, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.scienceLabSection1 = Section.objects.create(Class=self.science, assignedUser=self.charlie, sectionNumber=3,
                                                         sectionType='Lab', monday=False, tuesday=True, wednesday=False,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
        self.scienceLabSection2 = Section.objects.create(Class=self.science, assignedUser=self.charlie, sectionNumber=4,
                                                         sectionType='Lab', monday=False, tuesday=False, wednesday=True,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
        self.englishDiscussionSection1 = Section.objects.create(Class=self.english, assignedUser=self.alice,
                                                                sectionNumber=1, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.englishDiscussionSection2 = Section.objects.create(Class=self.english, assignedUser=self.bob,
                                                                sectionNumber=2, sectionType='Discussion', monday=True,
                                                                tuesday=False, wednesday=True, thursday=False,
                                                                friday=False, startTime=time(8, 0, 0),
                                                                endTime=time(9, 30, 0))
        self.englishLabSection1 = Section.objects.create(Class=self.english, assignedUser=self.charlie, sectionNumber=3,
                                                         sectionType='Lab', monday=False, tuesday=True, wednesday=False,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
        self.englishLabSection2 = Section.objects.create(Class=self.english, assignedUser=self.charlie, sectionNumber=4,
                                                         sectionType='Lab', monday=False, tuesday=False, wednesday=True,
                                                         thursday=False, friday=False, startTime=time(13, 0, 0),
                                                         endTime=time(14, 30, 0))
    def test_DeleteSection(self):
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 4)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {'thisCourseSections': "math"}, follow=True)
        self.client.post("/sections/", {'deleteSection': "1"}, follow=True)
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 4)

    def test_DeleteNewSection(self):
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 4)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {'thisCourseSections': "math"}, follow=True)
        self.client.post("/sections/", {'deleteSection': "2354"}, follow=True)
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 8)

    def test_DeleteNotExistSection(self):
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 4)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/courses/", {'thisCourseSections': "math"}, follow=True)
        self.client.post("/sections/", {'deleteSection': "34563456"}, follow=True)
        aliceSections = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSections), 7)