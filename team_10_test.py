import unittest
import Hospital as team_10
import os

class TestHospital(unittest.TestCase):
    def SetUp(self):
        self.app = team_10.Application()

    def test_Is_exist(self):
        self.assertEqual(team_10.test_is_exist("315196311"),True,"worker already there")
        self.assertEqual(team_10.test_is_exist("31681646"),False,"worker not there")

    def test_change_availability(self):
        flag = team_10.change_availability(True)
        self.assertIsNone(flag,"should be True")
        flag = team_10.change_availability(False)
        self.assertIsNone(flag,"should be False")

    def test_change_bg_color(self):
        file_test = open("testing.txt","r")
        dict = {"test":"not red"}
        item=["test"]
        dict = team_10.change_bg_color_of_inventory(dict,item,"testing.txt")
        self.assertEqual(dict["test"],"red","should be red")
        file_test.close()

    def test_is_item_exists(self):
        items = team_10.check_if_item_exist("test","testing.txt")
        self.assertTrue(items,"should have test in file")
        items = team_10.check_if_item_exist("mop","testing.txt")
        self.assertFalse(items,"should NOT have mop in file")

    def test_login(self):
        self.assertTrue(team_10.login_test('a','a',"b","b"),"should be true Same values")
        self.assertFalse(team_10.login_test("d","c","d","c"),"should be false Different values")

    def test_logout(self):
        team_10.logout()
        self.assertEqual(0,team_10.last_ID)

    def test_remove_worker(self):
        string="worker 123456 123 israel israeli"
        db = open('testing_remove.txt', 'a')
        db.write(string)
        db.close()
        self.assertTrue(team_10.remove_worker_from_database("123456","testing_remove.txt"),"The employee was found and deleted")
        self.assertFalse(team_10.remove_worker_from_database("987654", "testing_remove.txt"),"ID of a clerk and not a cleaning worker")

    def test_show_path(self):
        #check if there is any line in the file that not need to appear as work path.
        #if it wont work then we see a button of "go to sleep"
        list_path = team_10.test_show_path()
        self.assertFalse('go to sleep' in list_path, "Should not be here")
        self.assertFalse('worker 123 123 dor dor' in list_path, "Should not be here")
        self.assertFalse('clean bed' in list_path, "Should not be here")

    def test_view_notifications_clean_bed(self):
        #check if there is any line that not need to apear as notifications.
        # if it wont work then we see a button of "go to sleep"
        clean_beds = team_10.test_view_notifications_clean_bed()
        self.assertFalse('go to sleep' in clean_beds, "Should not be here")
        self.assertFalse('worker 123 123 dor dor' in clean_beds, "Should not be here")
        self.assertFalse('clean Floor 1' in clean_beds, "Should not be here")

    def test_view_notifications_clean_place(self):
        #check if there is any line that not need to apear as notifications.
        # if it wont work then we see a button of "go to sleep"
        clean_place = team_10.test_view_notifications_clean_place()
        self.assertFalse('go to sleep' in clean_place, "Should not be here")
        self.assertFalse('worker 123 123 dor dor' in clean_place, "Should not be here")
        self.assertTrue('clean Floor 1' in clean_place, "Should not be here")

    def test_view_notifications_deficients(self):
        #check if there is any line that not need to apear as notifications.
        # if it wont work then we see a button of "go to sleep"
        deficients = team_10.test_view_notifications_deficients()
        self.assertFalse('go to sleep' in deficients, "Should not be here")
        self.assertFalse('worker 123 123 dor dor' in deficients, "Should not be here")
        self.assertFalse('clean Floor 1' in deficients, "Should not be here")

    def test_update_work_path(self):
        #check that the new work path is updated and its in line 2
        team_10.test_update_work_path("test_notifications","Test1 Test2 Test3")
        with open("test_notifications.txt", "r") as file:
            file.seek(0)
            self.assertEqual(file.readline(), "worker 1234 1234 dor dor\n")
            self.assertEqual(file.readline(), "Test1 Test2 Test3\n")

    def test_update_manager_file(self):
        # Arrange
        details_report = "This is a test report."

        # Act
        team_10.test_update_manager_file(details_report)

        # Assert
        with open(f"test_report.txt", "r") as file:
            contents = file.read()
            self.assertEqual(contents, details_report)
            self.assertNotEqual(contents, details_report + 'test')
            self.assertNotEqual(contents, 'Previous test')

    if __name__ == '__main__':
        unittest.main()
