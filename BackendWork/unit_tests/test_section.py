from django.test import TestCase
from BackendWork.models import Section, MyUser, ClassList
from _datetime import time

class SectionUnitTestSuite(TestCase):
    def setUp(self):
        self.alice = MyUser.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890', role='Teaching Assistant')
        self.bob = MyUser.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891', role='Teaching Assistant')
        self.charlie = MyUser.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892', role='Teaching Assistant')
        self.theProfessor = MyUser.objects.create(username='professor', password='badpassword', name='professor', email='professor@yahoo.com', address='uwmcampus', phone='123-456-7893', role='Instructor')
        self.math = ClassList.objects.create(name='math', term='Fall', year=2022)
        self.history = ClassList.objects.create(name='history', term='Winter', year=2022)
        self.science = ClassList.objects.create(name='science', term='Spring', year=2023)
        self.english = ClassList.objects.create(name='english', term='Summer', year=2023)
        self.mathDiscussionSection1 = Section.objects.create(Class=self.math, assignedUser=self.alice, sectionNumber=1, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.mathDiscussionSection2 = Section.objects.create(Class=self.math, assignedUser=self.bob, sectionNumber=2, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.mathLabSection1 = Section.objects.create(Class=self.math, assignedUser=self.charlie, sectionNumber=3, sectionType='Lab', monday=False, tuesday=True, wednesday=False, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.mathLabSection2 = Section.objects.create(Class=self.math, assignedUser=self.charlie, sectionNumber=4, sectionType='Lab', monday=False, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.historyDiscussionSection1 = Section.objects.create(Class=self.history, assignedUser=self.alice, sectionNumber=1, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.historyDiscussionSection2 = Section.objects.create(Class=self.history, assignedUser=self.bob, sectionNumber=2, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.historyLabSection1 = Section.objects.create(Class=self.history, assignedUser=self.charlie, sectionNumber=3, sectionType='Lab', monday=False, tuesday=True, wednesday=False, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.historyLabSection2 = Section.objects.create(Class=self.history, assignedUser=self.charlie, sectionNumber=4, sectionType='Lab', monday=False, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.scienceDiscussionSection1 = Section.objects.create(Class=self.science, assignedUser=self.alice, sectionNumber=1, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False,startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.scienceDiscussionSection2 = Section.objects.create(Class=self.science, assignedUser=self.bob, sectionNumber=2, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.scienceLabSection1 = Section.objects.create(Class=self.science, assignedUser=self.charlie, sectionNumber=3, sectionType='Lab', monday=False, tuesday=True, wednesday=False, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.scienceLabSection2 = Section.objects.create(Class=self.science, assignedUser=self.charlie, sectionNumber=4, sectionType='Lab', monday=False, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.englishDiscussionSection1 = Section.objects.create(Class=self.english, assignedUser=self.alice, sectionNumber=1, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.englishDiscussionSection2 = Section.objects.create(Class=self.english, assignedUser=self.bob, sectionNumber=2, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(8, 0, 0), endTime=time(9, 30, 0))
        self.englishLabSection1 = Section.objects.create(Class=self.english, assignedUser=self.charlie, sectionNumber=3, sectionType='Lab', monday=False, tuesday=True, wednesday=False, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))
        self.englishLabSection2 = Section.objects.create(Class=self.english, assignedUser=self.charlie, sectionNumber=4, sectionType='Lab', monday=False, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(13, 0, 0), endTime=time(14, 30, 0))

    def test_list_section_length(self):
        aliceSectionList = Section.objects.filter(assignedUser=self.alice)
        bobSectionList = Section.objects.filter(assignedUser=self.bob)
        charlieSectionList = Section.objects.filter(assignedUser=self.charlie)
        self.assertEqual(len(aliceSectionList), 4, msg='Section failed to filter by TA')
        self.assertEqual(len(bobSectionList), 4, msg='Section failed to filter by TA')
        self.assertEqual(len(charlieSectionList), 8, msg='Section failed to filter by TA')

    def test_list_section_names_by_TA(self):
        aliceSectionList = list(Section.objects.filter(assignedUser=self.alice))
        bobSectionList = list(Section.objects.filter(assignedUser=self.bob))
        charlieSectionList = list(Section.objects.filter(assignedUser=self.charlie))
        self.assertEqual(aliceSectionList, [self.mathDiscussionSection1, self.historyDiscussionSection1, self.scienceDiscussionSection1, self.englishDiscussionSection1], msg='Section failed to filter by TA')
        self.assertEqual(bobSectionList, [self.mathDiscussionSection2, self.historyDiscussionSection2, self.scienceDiscussionSection2, self.englishDiscussionSection2], msg='Section failed to filter by TA')
        self.assertEqual(charlieSectionList, [self.mathLabSection1, self.mathLabSection2, self.historyLabSection1, self.historyLabSection2, self.scienceLabSection1, self.scienceLabSection2, self.englishLabSection1, self.englishLabSection2], msg='Section failed to filter by TA')

    def test_list_section_names_by_Class(self):
        mathSectionList = list(Section.objects.filter(Class=self.math))
        historySectionList = list(Section.objects.filter(Class=self.history))
        scienceSectionList = list(Section.objects.filter(Class=self.science))
        englishSectionList = list(Section.objects.filter(Class=self.english))
        self.assertEqual(mathSectionList, [self.mathDiscussionSection1, self.mathDiscussionSection2, self.mathLabSection1, self.mathLabSection2], msg='Section failed to filter by class')
        self.assertEqual(historySectionList, [self.historyDiscussionSection1, self.historyDiscussionSection2, self.historyLabSection1, self.historyLabSection2], msg='Section failed to filter by class')
        self.assertEqual(scienceSectionList, [self.scienceDiscussionSection1, self.scienceDiscussionSection2, self.scienceLabSection1, self.scienceLabSection2], msg='Section failed to filter by class')
        self.assertEqual(englishSectionList, [self.englishDiscussionSection1, self.englishDiscussionSection2, self.englishLabSection1, self.englishLabSection2], msg='Section failed to filter by class')

    def test_list_section_names_by_Type(self):
        discussionSectionList = list(Section.objects.filter(sectionType='Discussion'))
        labSectionList = list(Section.objects.filter(sectionType='Lab'))
        self.assertEqual(discussionSectionList, [self.mathDiscussionSection1, self.mathDiscussionSection2, self.historyDiscussionSection1, self.historyDiscussionSection2, self.scienceDiscussionSection1, self.scienceDiscussionSection2, self.englishDiscussionSection1, self.englishDiscussionSection2], msg='Section failed to filter by section type')
        self.assertEqual(labSectionList, [self.mathLabSection1, self.mathLabSection2, self.historyLabSection1, self.historyLabSection2, self.scienceLabSection1, self.scienceLabSection2, self.englishLabSection1, self.englishLabSection2], msg='Section failed to filter by section type')

    def test_edit_section_TA(self):
        self.mathDiscussionSection1.TA = self.bob
        self.assertEqual(self.mathDiscussionSection1.TA, self.bob, msg='Section failed to update TA')

    def test_edit_section_type(self):
        self.mathDiscussionSection1.sectionType = 'Lab'
        self.assertEqual(self.mathDiscussionSection1.sectionType, 'Lab', msg='Section failed to update section type')

    def test_edit_section_number(self):
        self.mathDiscussionSection1.sectionNumber = 9
        self.assertEqual(self.mathDiscussionSection1.sectionNumber, 9, msg='Section failed to update section number')

    def test_edit_section_class(self):
        self.mathDiscussionSection1.Class = self.history
        self.assertEqual(self.mathDiscussionSection1.Class, self.history, msg='Section failed to update class')

    def test_edit_section_schedule(self):
        self.mathDiscussionSection1.schedule = ['Tuesday']
        self.assertEqual(self.mathDiscussionSection1.schedule, ['Tuesday'], msg='Section failed to update schedule')

    def test_edit_section_start_time(self):
        self.mathDiscussionSection1.startTime = time(1, 0, 0)
        self.assertEqual(self.mathDiscussionSection1.startTime, time(1, 0, 0), msg='Section failed to update start time')

    def test_edit_section_end_time(self):
        self.mathDiscussionSection1.endTime = time(23, 0, 0)
        self.assertEqual(self.mathDiscussionSection1.endTime, time(23, 0, 0), msg='Section failed to update end time')

    def test_create_section(self):
        self.newMathDiscussion = Section.objects.create(Class=self.math, assignedUser=self.alice, sectionNumber=1, sectionType='Discussion', monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, startTime=time(12, 0, 0), endTime=time(13, 30, 0))
        aliceSectionList = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSectionList), 5, msg='Section failed to create a new record')

    def test_delete_section(self):
        self.mathDiscussionSection1.delete()
        aliceSectionList = Section.objects.filter(assignedUser=self.alice)
        self.assertEqual(len(aliceSectionList), 3, msg='Section failed to delete a record')