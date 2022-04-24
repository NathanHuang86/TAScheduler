# from django.test import TestCase
# from BackendWork.models import User, PermissionAssignment, Permission
#
# class PermissionUnitTestSuite(TestCase):
#     def setUp(self):
#         self.alice = User.objects.create(username='alice', password='password', name='alice', email='alice@yahoo.com', address='somewhere', phone='123-456-7890')
#         self.bob = User.objects.create(username='bob', password='password123', name='bob', email='bob@yahoo.com', address='someplace', phone='123-456-7891')
#         self.charlie = User.objects.create(username='charlie', password='123password', name='charlie', email='charlie@yahoo.com', address='sometown', phone='123-456-7892')
#         self.dennis = User.objects.create(username='dennis', password='password!', name='dennis', email='dennis@yahoo.com', address='milwaukee', phone='123-456-7893')
#
#         self.readPermission = Permission.objects.create(API_Name='READ_ACCESS', label='read_access')
#         self.writePermission = Permission.objects.create(API_Name='WRITE_ACCESS', label='write_access')
#         self.executePermission = Permission.objects.create(API_Name='EXECUTE_ACCESS', label='execute_access')
#
#         self.alicePermissionAssignment = PermissionAssignment.objects.create(userID=self.alice, permission=self.readPermission)
#
#         self.bobPermissionAssignment = PermissionAssignment.objects.create(userID=self.charlie, permission=self.readPermission)
#         self.bobPermissionAssignment = PermissionAssignment.objects.create(userID=self.charlie, permission=self.writePermission)
#
#         self.charliePermissionAssignment = PermissionAssignment.objects.create(userID=self.charlie, permission=self.readPermission)
#         self.charliePermissionAssignment = PermissionAssignment.objects.create(userID=self.charlie, permission=self.writePermission)
#         self.charliePermissionAssignment = PermissionAssignment.objects.create(userID=self.charlie, permission=self.executePermission)
#
#     def test_list_class_length(self):
#         charliePermissionList = P.objects.filter(owner = self.charlie)
#         self.assertEqual(len(charlieClassList), 2)