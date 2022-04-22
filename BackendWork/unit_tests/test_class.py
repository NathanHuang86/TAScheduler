from django.test import TestCase
from BackendWork.models import Class, User

class ClassUnitTestSuite(TestCase):
    def setUp(self):
        self.alice = User.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890')
        self.bob = User.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891')
        self.charlie = User.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892')
        self.math = Class.objects.create(name='math', owner=self.alice)
        self.history = Class.objects.create(name='history', owner=self.bob)
        self.science = Class.objects.create(name='science', owner=self.charlie)
        self.english = Class.objects.create(name='english', owner=self.charlie)

    def test_list_class_length(self):
        charlieClassList = Class.objects.filter(owner = self.charlie)
        self.assertEqual(len(charlieClassList), 2)

    def test_list_class_names(self):
        charlieClassList = Class.objects.filter(owner = self.charlie)
        self.assertEqual(charlieClassList, [self.science, self.english])

    def test_edit_owner(self):
        self.history.owner = self.charlie
        self.assertEqual(self.charlie, self.history.owner)

    def test_edit_class_name(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name)

    def test_delete_class(self):
        self.science.delete()
        charlieClassList = Class.objects.filter(owner=self.charlie)
        self.assertEqual(1, len(charlieClassList))

    def test_create_class(self):
        self.english2 = Class.objects.create(name='english2', owner=self.charlie)
        charlieClassList = Class.objects.filter(owner=self.charlie)
        self.assertEqual(3, len(charlieClassList))


