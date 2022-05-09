from django.test import TestCase
from BackendWork.models import ClassList, MyUser

class ClassListUnitTestSuite(TestCase):
    def setUp(self):
        self.math = ClassList.objects.create(name='math', term='Fall', year=2022)
        self.history = ClassList.objects.create(name='history', term='Winter', year=2022)
        self.science = ClassList.objects.create(name='science', term='Spring', year=2023)
        self.english = ClassList.objects.create(name='english', term='Summer', year=2023)

    def test_list_classlist_length(self):
        classList2022 = ClassList.objects.filter(year=2022)
        self.assertEqual(len(classList2022), 2, msg='ClassList failed to filter by year')

    def test_list_classlist_year(self):
        classList2023 = list(ClassList.objects.filter(year=2023))
        self.assertEqual(classList2023, [self.science, self.english], msg='ClassList failed to filter by year')

    def test_list_classlist_term(self):
        classListFall = list(ClassList.objects.filter(term='Fall'))
        self.assertEqual(classListFall, [self.math], msg='ClassList failed to filter by year')

    def test_list_classlist_name(self):
        classListMath = list(ClassList.objects.filter(name='math'))
        self.assertEqual(classListMath, [self.math], msg='ClassList failed to filter by name')

    def test_edit_classlist_name(self):
        self.history.name = 'US history'
        self.assertEqual('US history', self.history.name, msg='ClassList failed to edit name')

    def test_edit_classlist_term(self):
        self.history.term = 'Fall'
        self.assertEqual('Fall', self.history.term, msg='ClassList failed to edit term')

    def test_edit_classlist_year(self):
        self.history.year = 2024
        self.assertEqual(2024, self.history.year, msg='ClassList failed to edit year')

    def test_delete_classlist(self):
        self.science.delete()
        classListSpring = ClassList.objects.filter(term='Spring')
        self.assertEqual(0, len(classListSpring), msg='ClassList failed to delete a record')

    def test_create_classlist(self):
        self.english2 = ClassList.objects.create(name='english2', term='Fall', year=2022)
        classListFall = ClassList.objects.filter(term='Fall')
        self.assertEqual(2, len(classListFall), msg='ClassList failed to create a record')