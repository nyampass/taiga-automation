import unittest
from task import passed
import datetime as dt

now = dt.datetime(2024,3,9,10,18)
class TaskTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_not_passed_yet(self):
        self.assertFalse(passed("19 10 9 3"),now)
    def test_already_passed(self):
        self.assertTrue(passed("49 9 9 3"),now)
    def test_just_passed(self):
        self.assertTrue(passed("18 10 9 3"),now)
    # def test_passed_loop(self):
    #     now = dt.datetime.now()
    #     correct = True
    #     for i in range(min(now.minute+2,59)):
    #         if  (max(now.minute-30,0)<i) and (i<now.minute) and (not passed(f"{i} {now.hour} {now.day} {now.month}",now)):
    #             correct = False
    #             break
    #     self.assertTrue(correct)

if __name__ == "__main__":
    unittest.main()
