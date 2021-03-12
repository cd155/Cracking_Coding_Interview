# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.
# A Permutation of a string:another string that contains same characters, but they can have different orders, 
# only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.

# Please ask interviewer about whether blank spaces or case sensitive need to be considered.
# "dog    " and "    god" or "Dog" and "dog"

# The following examples exclude condtions with blank spaces and case sensitive.

# Solution: ideally we can use a hash table to track permutation of a string


def check_permutation_brutefoce(string_one, string_two):
    if len(string_one) != len(string_two):
        return False

    for char_one in string_one:
        checker = False
        for char_two in string_two:
            if char_one == char_two:
                string_two.replace(char_two, '', 1)
                checker = True
        if not checker:
            return False
    return True

def check_permutation_hash(string_one, string_two):
    dict_table_one = {}
    if len(string_one) != len(string_two):
        return False

    # Add string one into dictionary
    for char in string_one:
        if char not in dict_table_one:
            dict_table_one[char] = 1
        else: 
            dict_table_one[char] = dict_table_one[char] + 1
    # check whether char in the dictionary
    for char in string_two:
        if char in dict_table_one and dict_table_one[char] != 0:
            dict_table_one[char] = dict_table_one[char] - 1
        else:
            return False
    return sum(dict_table_one.values()) == 0

import unittest
class TestIsPermutation(unittest.TestCase):
    def setUp(self):
        self.sample_is_permutation = [["abcd","cbda"],["hello", "lhole"],["acemybest","bestmyace"]]
        self.sample_is_not_permutation = [["","a"],["b",""],["mcmaster","masterma"],["a","b"],["zc","z!"]]

    def tearDown(self):
        self.sample_is_permutation = None
        self.sample_is_not_permutation = None

    def test_is_permutation_brutefoce(self):
        for item in self.sample_is_permutation:
            self.assertTrue(check_permutation_brutefoce(item[0], item[1]))

    def test_is_not_permutation_brutefoce(self):
        for item in self.sample_is_not_permutation:
            self.assertFalse(check_permutation_brutefoce(item[0], item[1]))

    def test_is_permutation_hash(self):
        for item in self.sample_is_permutation:
            self.assertTrue(check_permutation_hash(item[0], item[1]))

    def test_is_not_permutation_hash(self):
        for item in self.sample_is_not_permutation:
            self.assertFalse(check_permutation_hash(item[0], item[1]))

if __name__ == '__main__':
    unittest.main()
