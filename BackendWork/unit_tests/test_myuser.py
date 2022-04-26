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
        self.assertEqual(len(adminList), 2, msg='MyUser failed to filter by role')
        self.assertEqual(len(instructorList), 2, msg='MyUser failed to filter by role')
        self.assertEqual(len(teachingAssistantList), 2, msg='MyUser failed to filter by role')

    def test_list_myuser_names(self):
        adminList = list(MyUser.objects.filter(role='Admin'))
        instructorList = list(MyUser.objects.filter(role='Instructor'))
        teachingAssistantList = list(MyUser.objects.filter(role='Teaching Assistant'))
        self.assertEqual(adminList, [self.charlie, self.dennis], msg='MyUser failed to filter by role')
        self.assertEqual(instructorList, [self.bob, self.ellis], msg='MyUser failed to filter by role')
        self.assertEqual(teachingAssistantList, [self.alice, self.felix], msg='MyUser failed to filter by role')

    def test_edit_username(self):
        self.alice.username = 'arial'
        self.assertEqual('arial', self.alice.username, msg='MyUser failed to edit username')

    def test_edit_password(self):
        self.alice.password = 'password@'
        self.assertEqual('password@', self.alice.password, msg='MyUser failed to edit password')

    def test_edit_name(self):
        self.alice.name = 'arial'
        self.assertEqual('arial', self.alice.name, msg='MyUser failed to edit name')

    def test_edit_email(self):
        self.alice.name = 'alice@gmail.com'
        self.assertEqual('alice@gmail.com', self.alice.name, msg='MyUser failed to edit email')

    def test_edit_address(self):
        self.alice.address = 'nowhere'
        self.assertEqual('nowhere', self.alice.address, msg='MyUser failed to edit address')

    def test_edit_phone(self):
        self.alice.phone = '0987654321'
        self.assertEqual('0987654321', self.alice.phone, msg='MyUser failed to edit phone')

    def test_delete_myuser(self):
        self.alice.delete()
        teachingAssistantList = MyUser.objects.filter(role='Teaching Assistant')
        self.assertEqual(1, len(teachingAssistantList), msg='MyUser failed to delete a record')

    def test_create_myuser(self):
        self.garry = MyUser.objects.create(username='garry', password='password!#', name='garry', email='garry@yahoo.com', address='middleonowhere', phone='123-456-7896', role='Admin')
        adminList = MyUser.objects.filter(role='Admin')
        self.assertEqual(3, len(adminList), msg='MyUser failed to create a record')