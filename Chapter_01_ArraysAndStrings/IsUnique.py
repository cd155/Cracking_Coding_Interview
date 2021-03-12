# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def is_unique_hash(test_string):
    dict_table = {}
    for char in test_string:
        if char in dict_table:
            return False
        else:
            dict_table[char] = True
    return True

def is_unique_array(test_string):
    bool_array = [False] * 128
    for char in test_string:
        if ord(char) > 128:
            print ("Array: Out of bound in " + test_string)
            return False

        if bool_array[ord(char)]:
            return False
        else:
            bool_array[ord(char)] = True
    return True

def is_unique_bit_array(test_string):
    # check the following if you have some troubles to understand the bit vector solution
    # https://stackoverflow.com/questions/9141830/explain-the-use-of-a-bit-vector-for-determining-if-all-characters-are-unique
    pass


import unittest
class TestIsUniqueCase(unittest.TestCase):
    def setUp(self):
        self.sample_is_unique = ["algorithm", "", "h", "DonaldTrump", "Tt", "12ad好"]
        self.sample_is_not_unique = ["additional", "2020", "12zz明", "listening"]

    def tearDown(self):
        self.sample_is_unique = None
        self.sample_is_not_unique = None

    def test_is_unique_hash_true(self):
        for item in self.sample_is_unique:
            self.assertTrue(is_unique_hash(item))
    
    def test_is_unique_hash_false(self):
        for item in self.sample_is_not_unique:
            self.assertFalse(is_unique_hash(item))
    
    def test_is_unique_array_true(self):
        for item in self.sample_is_unique:
            self.assertTrue(is_unique_array(item))
    
    def test_is_unique_array_false(self):
        for item in self.sample_is_not_unique:
            self.assertFalse(is_unique_array(item))

if __name__ == '__main__':
    unittest.main()
