import unittest
import team_10


class TestHospital(unittest.TestCase):
    def SetUp(self):
        self.app = team_10.Application()
    def test_is_exist(self):
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
    def test_is_item_exists(self):
        items = team_10.check_if_item_exist("test","testing.txt")
        self.assertTrue(items,"should have test in file")
        items = team_10.check_if_item_exist("mop","testing.txt")
        self.assertFalse(items,"should NOT have mop in file")
    if __name__ == '__main__':
        unittest.main()