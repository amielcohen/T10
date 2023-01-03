import unittest
import team_10


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



    if __name__ == '__main__':
        unittest.main()