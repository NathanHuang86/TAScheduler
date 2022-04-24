from django.test import TestCase
from BackendWork.models import MyUser

class MyUserUnitTestSuite(TestCase):
    def setUp(self) -> None:
        self.alice = MyUser.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890', role='Teaching Assistant')
        self.bob = MyUser.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891', role='Instructor')
        self.charlie = MyUser.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892', role='Admin')
        self.dennis = MyUser.objects.create(username='dennis', password='password!', name='dennis', email='dennis@yahoo.com', address='milwaukee', phone='123-456-7893', role='Admin')
        self.ellis = MyUser.objects.create(username='ellis', password='badpassword', name='ellis', email='ellis@yahoo.com', address='wheretheylive', phone='123-456-7894', role='Instructor')
        self.felix = MyUser.objects.create(username='felix', password='badpassword1', name='felix', email='felix@yahoo.com', address='nowhere', phone='123-456-7895', role='Teaching Assistant')

    def test_list_myuser_length(self):
        adminList = MyUser.objects.filter(role='Admin')
        instructorList = MyUser.objects.filter(role='Instructor')
        teachingAssistantList = MyUser.objects.filter(role='Teaching Assistant')
        self.assertEqual(len(adminList), 2)
        self.assertEqual(len(instructorList), 2)
        self.assertEqual(len(teachingAssistantList), 2)

    def test_list_myuser_names(self):
        adminList = MyUser.objects.filter(role='Admin')
        instructorList = MyUser.objects.filter(role='Instructor')
        teachingAssistantList = MyUser.objects.filter(role='Teaching Assistant')
        self.assertEqual(adminList, [self.charlie, self.dennis])
        self.assertEqual(instructorList, [self.bob, self.ellis])
        self.assertEqual(teachingAssistantList, [self.alice, self.felix])

    def test_edit_username(self):
        self.alice.username = 'newalice'
        self.assertEqual(self.alice.username, 'newalice')

    def test_edit_password(self):
        self.alice.password = 'newpassword123'
        self.assertEqual('newpassword123', self.alice.password)

    def test_edit_name(self):
        self.alice.name = 'alexa'
        self.assertEqual('alexa', self.alice.name)

    def test_edit_email(self):
        self.alice.email = 'alice@gmail.com'
        self.assertEqual('alice@gmail.com', self.alice.email)

    def test_edit_address(self):
        self.alice.address = 'milwaukeecampus'
        self.assertEqual('milwaukeecampus', self.alice.address)

    def test_edit_phone(self):
        self.alice.phone = '123-123-1234'
        self.assertEqual('123-123-1234', self.alice.phone)

    def test_delete_myuser(self):
        self.alice.delete()
        teachingAssistantList = MyUser.objects.filter(role='Teaching Assistant')
        self.assertEqual(1, len(teachingAssistantList))

    def test_create_myuser(self):
        self.garry = MyUser.objects.create(username='garry', password='somepassword', name='garry', email='garry@yahoo.com', address='garryshome', phone='123-456-7896', role='Teaching Assistant')
        teachingAssistantList = MyUser.objects.filter(role='Teaching Assistant')
        self.assertEqual(3, len(teachingAssistantList))