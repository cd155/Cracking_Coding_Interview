# Check Substring: 
# Given two strings,write a method to decide if one is a substring of the other.

def check_substring(string_one, string_two):
    if len(string_one) > len(string_two):
        return pair_string(string_one, string_two)
    else:
        return pair_string(string_two, string_one)

def pair_string(string_long, string_short):
    if len(string_short) == 0:
        return False

    for i in range(len(string_long)):
        base = string_long[i:i+len(string_short)]
        if base == string_short:
            return True
    return False

import unittest
class TestIsSubstring(unittest.TestCase):
    def setUp(self):
        self.sample_is_substring = [["abbcaaade","aaa"],["thisis","is"],["happymorning","mor"]]
        self.sample_is_not_substring = [["",""],["","ab"],["a","b"],["happymorning","where"]]

    def tearDown(self):
        self.sample_is_substring = None
        self.sample_is_not_substring = None

    def test_is_substring(self):
        for item in self.sample_is_substring:
            self.assertTrue(check_substring(item[0], item[1]))

    def test_is_not_substring(self):
        for item in self.sample_is_not_substring:
            self.assertFalse(check_substring(item[0], item[1]))

if __name__ == '__main__':
    unittest.main()