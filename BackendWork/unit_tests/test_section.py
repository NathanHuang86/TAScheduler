from django.test import TestCase
from BackendWork.models import Section, MyUser, ClassList

class SectionUnitTestSuite(TestCase):
    def setUp(self):
        self.alice = MyUser.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890', role='Teaching Assistant')
        self.bob = MyUser.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891', role='Teaching Assistant')
        self.charlie = MyUser.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892', role='Teaching Assistant')
        self.theProfessor = MyUser.objects.create(username='professor', password='badpassword', name='professor', email='professor@yahoo.com', address='uwmcampus', phone='123-456-7893', role='Instructor')
        self.math = ClassList.objects.create(name='math', owner=self.theProfessor)
        self.history = ClassList.objects.create(name='history', owner=self.theProfessor)
        self.science = ClassList.objects.create(name='science', owner=self.theProfessor)
        self.english = ClassList.objects.create(name='english', owner=self.theProfessor)
        self.mathDiscussionSection = Section.objects.create(Class=self.math, TA=self.alice)


# class Section(models.Model):
#     SCHEDULE_CHOICES = (('Sunday', 'SUNDAY'), ('Monday', 'MONDAY'), ('Tuesday', 'TUESDAY'), ('Wednesday', 'WEDNESDAY'), ('Thursday', 'THURSDAY'), ('Friday', 'FRIDAY'), ('Saturday', 'SATURDAY'))
#     SECTION_TYPE_CHOICES = (('Discussion', 'DISCUSSION'), ('Lab', 'LAB'))
#     Class = models.ForeignKey(ClassList, on_delete=models.SET_NULL, null=False)
#     TA = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=False)
#     sectionNumber = models.IntegerField
#     sectionType = models.CharField(choices=SECTION_TYPE_CHOICES)
#     schedule = MultiSelectField(choices=SCHEDULE_CHOICES)
#     startTime = models.TimeField
#     endTime = models.TimeField