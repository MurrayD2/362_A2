# Daniel Murray
# MURRAYD2
# 12 November 2023
# CS362 A2: Simple Test-Driven Development activity

import unittest
from check_pwd import check_pwd


class TestAvgList(unittest.TestCase):
    def test1(self):
        """Verifies that a string of fewer than 8 characters returns False
        """
        pwd = "0"
        self.assertFalse(check_pwd(pwd), msg="Short password should be False")


if __name__ == '__main__':
    unittest.main(verbosity=2)
