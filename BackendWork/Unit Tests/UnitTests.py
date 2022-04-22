from django.test import TestCase
from Skeleton import Account, Assignment, Course, Lab, TA, Instructor, Supervisor

class AccountVerify(TestCase):
    def test0(self):
        pass #test positive case

    def test1(self):
        pass #test string1 doesnt match

    def test2(self):
        pass #test string2 doesnt match

    def test3(self):
        pass #test neither string matches

    def test4(self):
        pass #test too many arguments

    def test5(self):
        pass #test too few arguments

    def test6(self):
        pass #test wrong type of argument

class CourseViewAssignment(TestCase):
    def test0(self):
        pass #test TA

    def test1(self):
        pass #test Instructor

    def test2(self):
        pass #test Supervisor

class LabViewAssignment(TestCase):
    def test0(self):
        pass #test TA

    def test1(self):
        pass #test Instructor

    def test2(self):
        pass #test Supervisor

class TAViewInfo(TestCase):
    def test0(self):
        pass #test positive case

    def test1(self):
        pass #test no info for given user

    def test2(self):
        pass #test no matching TA

    def test3(self):
        pass #test too few arguments

    def test4(self):
        pass #test too many arguments

    def test5(self):
        pass #test wrong type of argument

class TAEditInfo(TestCase):
    def test0(self):
        name = "Bob"
        print(name)
        TA(name)
        TA.editInfo()
        self.assertEqual(TA.name, "newBob", msg="")


class SupervisorCreateCourse(TestCase):
    def test0(self):
        pass #test positive case

    def test1(self):
        pass #test too few arguments

    def test2(self):
        pass #test too many arguments

    def test3(self):
        pass #wrong type of arguments

    def test4(self):
        pass #course name already exists

    def test5(self):
        pass #instructor already has a course

    def test6(self):
        pass