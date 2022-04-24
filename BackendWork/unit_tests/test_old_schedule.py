# from django.test import TestCase
# from BackendWork.models import Schedule
# import datetime
#
# class ScheduleUnitTestSuite(TestCase):
#     def setUp(self) -> None:
#         self.MWF1 = Schedule.objects.create(sunday=False, monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, saturday=False, startTime=datetime.time(6, 0, 0), endTime=datetime.time(6, 50, 0))
#         self.MWF2 = Schedule.objects.create(sunday=False, monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, saturday=False, startTime=datetime.time(8, 0, 0), endTime=datetime.time(8, 50, 0))
#         self.MWF3 = Schedule.objects.create(sunday=False, monday=True, tuesday=False, wednesday=True, thursday=False, friday=False, saturday=False, startTime=datetime.time(8, 30, 0), endTime=datetime.time(9, 20, 0))
#         self.TT1 = Schedule.objects.create(sunday=False, monday=False, tuesday=True, wednesday=False, thursday=True, friday=False, saturday=False, startTime=datetime.time(13, 0, 0), endTime=datetime.time(14, 15, 0))
#         self.TT2 = Schedule.objects.create(sunday=False, monday=False, tuesday=True, wednesday=False, thursday=True, friday=False, saturday=False, startTime=datetime.time(13, 0, 0), endTime=datetime.time(14, 15, 0))
#         self.TT3 = Schedule.objects.create(sunday=False, monday=False, tuesday=True, wednesday=False, thursday=True, friday=False, saturday=False, startTime=datetime.time(15, 0, 0), endTime=datetime.time(16, 15, 0))
#
#     def test_list_schedule_length(self):
#         mondaySchedules = Schedule.objects.filter(monday=True)
#         tuesdaySchedules = Schedule.objects.filter(tuesday=True)
#         afternoonClasses = Schedule.objects.filter(startTime=datetime.time(13, 0, 0))
#         self.assertEqual(len(mondaySchedules), 3)
#         self.assertEqual(len(tuesdaySchedules), 3)
#         self.assertEqual(len(afternoonClasses), 2)
#
#     def test_list_schedule_names(self):
#         mondaySchedules = Schedule.objects.filter(monday=True)
#         tuesdaySchedules = Schedule.objects.filter(tuesday=True)
#         self.assertEqual([self.MWF1, self.MWF2, self.MWF3], mondaySchedules)
#         self.assertEqual([self.TT1, self.TT2, self.TT3], tuesdaySchedules)
#
#     def test_edit_day(self):
#         self.MWF1.sunday = True
#         sundaySchedules = Schedule.objects.filter(sunday=True)
#         self.assertEqual(len(sundaySchedules), 1)
#
#     def test_edit_time(self):
#         self.MWF1.startTime = datetime.time(6, 30, 0)
#         morningClassSchedules = Schedule.objects.filter(startTime=datetime.time(6, 30, 0))
#         self.assertEqual(len(morningClassSchedules), 1)
#
#     def test_create_schedule(self):
#         self.Weekend = Schedule.objects.create(sunday=True, monday=False, tuesday=False, wednesday=False, thursday=False, friday=False, saturday=True, startTime=datetime.time(15, 0, 0), endTime=datetime.time(16, 0, 0))
#         weekendClassSchedules = Schedule.objects.filter(sunday=True)
#         self.assertEqual(len(weekendClassSchedules), 1)
#
#     def test_delete_schedule(self):
#         self.MWF1.delete()
#         mondaySchedules = Schedule.objects.filter(monday=True)
#         self.assertEqual(len(mondaySchedules), 2)
#
#
