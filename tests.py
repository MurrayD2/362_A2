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

    def test4(self):
        """Verifies that a valid pwd of length 20 passes
        """
        pwd = "aA1!asdf123456789012"
        self.assertTrue(check_pwd(pwd), msg="Password of length 20 should be "
                        "True")

    def test5(self):
        """Verifies that a password of valid length without a lowercase letter
        fails
        """
        pwd = "AA!ASDF12345"
        self.assertFalse(check_pwd(pwd), msg="Password without a lowercase "
                         "letter should fail")

    def test6(self):
        """Verifies that a password of valid length without an uppercase letter
        fails
        """
        pwd = "aa!asdf12345"
        self.assertFalse(check_pwd(pwd), msg="Password without an uppercase "
                         "letter should fail")

    def test7(self):
        """Verifies that a password of valid length without a number fails
        """
        pwd = "aa!asdfASDFER"
        self.assertFalse(check_pwd(pwd), msg="Password without a number "
                         "should fail")

    def test8(self):
        """Verifies that a password of valid length without a special character
        fails
        """
        pwd = "aa45asdfASDFER"
        self.assertFalse(check_pwd(pwd), msg="Password without a special "
                         "character should fail")

    def test9(self):
        """Verifies that a blank password fails
        """
        pwd = ""
        self.assertFalse(check_pwd(pwd), msg="Blank password should fail")


if __name__ == '__main__':
    unittest.main(verbosity=2)
