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

    def test_list_myuser_names(self):
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(charlieClassList, [self.science, self.english])

    def test_edit_username(self):
        self.history.owner = self.charlie
        self.assertEqual(self.charlie, self.history.owner)

    def test_edit_password(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_edit_name(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_edit_email(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_edit_address(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_edit_phone(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_delete_myuser(self):
        self.science.delete()
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(1, len(charlieClassList))

    def test_create_myuser(self):
        self.english2 = ClassList.objects.create(name='english2', owner=self.charlie)
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(3, len(charlieClassList))