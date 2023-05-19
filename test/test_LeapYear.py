from tools import is_leap_year
import unittest

class TestLeapYear(unittest.TestCase):
    def test_2023(self):
        result=is_leap_year(2020)
        self.assertEqual(result,False)
        
if __name__=='__main__':
    unittest.main()
