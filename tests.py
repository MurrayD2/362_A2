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

    def test2(self):
        """Verifies that a valid pwd of length 8 returns True
        """
        pwd = "aA1!asdf"
        self.assertTrue(check_pwd(pwd), msg="Password of length 8 should be "
                        "True")

    def test3(self):
        """Verifies that valid pwd of length longer than 20 returns False
        """
        pwd = "aA1!asdf12345678901234"
        self.assertFalse(check_pwd(pwd), msg="Password of length 22 should be "
                         "False")


if __name__ == '__main__':
    unittest.main(verbosity=2)
