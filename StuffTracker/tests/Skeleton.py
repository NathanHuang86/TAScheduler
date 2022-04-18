class AssignInterface:
    def assignTo(self, user, course):
        pass
    def notify(self):
        pass

class UserInterface:
    name = "todo"
    contact = "todo"
    phoneNumber = "todo"
    address = "todo"

    def viewInfo(self):
        pass

    def editInfo(self):
        pass

    def showUsers(self):
        pass

    def showAssignments(self):
        pass

class Account:
    username = "todo"
    password = "todo"
    def verify(self, string1, string2):
        pass

class Assignment:
    name = "todo"
    points = "todo"
    description = "todo"

class Course:
    def viewAssignment(self):
        pass

class Lab:
    def viewLabAssignment(self):
        pass

class TA(UserInterface):
    labs = "todo"

class Instructor(AssignInterface):
    courseTA = "todo"
    courseToTa = "todo"

class Supervisor(AssignInterface):
    courses = "todo"
    accounts = "todo"
    courseToLab = "todo"

    def createCourse(self, string1, instructor, labs):
        pass

    def editCourse(self, instructor, labs):
        pass

    def deleteCourse(self, course):
        pass

    def createAccount(self, string1, string2):
        pass

    def editAccount(self, Account):
        pass

    def deleteAccount(self, Account):
        pass

    def viewCourses(self):
        pass
