from django.test import TestCase
from BackendWork.models import MyUser
from django.test import Client

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
    def test_editUserName(self):
        alices = MyUser.objects.filter(username='alice')
        self.assertEqual(len(alices), 1)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/users/", {'editUser': "alice"}, follow=True)
        self.client.post("/users/", {'saveEditUser': "alice", 'username': "newUserName", 'role': "Teaching Assistant"}, follow=True)
        alices = MyUser.objects.filter(username='alice')
        newUserNames = MyUser.objects.filter(username='newUserName')
        self.assertEqual(len(alices), 0)
        self.assertEqual(len(newUserNames), 1)

    def test_editUserNameFailure(self):
        alices = MyUser.objects.filter(username='alice')
        self.assertEqual(len(alices), 1)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/users/", {'editUser': "alice"}, follow=True)
        self.client.post("/users/", {'saveEditUser': "alice", 'username': "Mike", 'role': "Teaching Assistant"}, follow=True)
        alices = MyUser.objects.filter(username='alice')
        mikes = MyUser.objects.filter(username='Mike')
        self.assertEqual(len(alices), 1)
        self.assertEqual(len(mikes), 1)

    def test_editUserNameFailure(self):
        alices = MyUser.objects.filter(username='alice')
        self.assertEqual(len(alices), 1)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/users/", {'editUser': "alice"}, follow=True)
        self.client.post("/users/", {'saveEditUser': "alice", 'username': "Mike", 'role': "Teaching Assistant"}, follow=True)
        alices = MyUser.objects.filter(username='alice')
        mikes = MyUser.objects.filter(username='Mike')
        self.assertEqual(len(alices), 1)
        self.assertEqual(len(mikes), 0)

    def test_editUserNoRole(self):
        alices = MyUser.objects.filter(username='alice')
        self.assertEqual(len(alices), 1)
        self.client.post("", {"username": "Mike", "password": "Mike"}, follow=True)
        self.client.post("/users/", {'editUser': "alice"}, follow=True)
        self.client.post("/users/", {'saveEditUser': "alice", 'username': "Mike"}, follow=True)
        alices = MyUser.objects.filter(username='alice')
        mikes = MyUser.objects.filter(username='Mike')
        self.assertEqual(len(alices), 1)
        self.assertEqual(len(mikes), 0)