from django.test import TestCase
from BackendWork.models import ClassList, MyUser

class ClassListUnitTestSuite(TestCase):
    def setUp(self):
        self.alice = MyUser.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890', role='Instructor')
        self.bob = MyUser.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891', role='Instructor')
        self.charlie = MyUser.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892', role='Instructor')
        self.math = ClassList.objects.create(name='math', owner=self.alice)
        self.history = ClassList.objects.create(name='history', owner=self.bob)
        self.science = ClassList.objects.create(name='science', owner=self.charlie)
        self.english = ClassList.objects.create(name='english', owner=self.charlie)

    def test_list_classlist_length(self):
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(len(charlieClassList), 2, msg='ClassList failed to filter by owner')

    def test_list_classlist_names(self):
        charlieClassList = list(ClassList.objects.filter(owner=self.charlie))
        self.assertEqual(charlieClassList, [self.science, self.english], msg='ClassList failed to filter by owner')

    def test_edit_owner(self):
        self.history.owner = self.charlie
        self.assertEqual(self.charlie, self.history.owner, msg='ClassList failed to edit owner')

    def test_edit_classlist_name(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name, msg='ClassList failed to edit name')

    def test_delete_classlist(self):
        self.science.delete()
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(1, len(charlieClassList), msg='ClassList failed to delete a record')

    def test_create_classlist(self):
        self.english2 = ClassList.objects.create(name='english2', owner=self.charlie)
        charlieClassList = ClassList.objects.filter(owner=self.charlie)
        self.assertEqual(3, len(charlieClassList), msg='ClassList failed to create a record')