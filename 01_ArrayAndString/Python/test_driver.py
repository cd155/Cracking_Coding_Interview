from pytest import *
from IsUnique import *
from CheckPermutation import *
from URLify import replace_spaces_expression
from PermutePalindrome import is_permute_palindrome_arr, isPermPalinDict
from OneAway import oneway_dict
from StringCompress import string_compress, compreStr
from RotateMatrix import rotate_matrix_with_degree
from ZeroMatrix import *
from StringRotate import is_rotate_string


# Is Unique
class TestIsUniqueCase:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.input1 = ["algorithm?", "12zz!?", "", "a", "oops", 
                       "thisgreat", "12!-!?", "123aaaaaaa!?", "ertushg819#@", "~triangle~", 
                       "mil~k", " this!2", "  "]
        self.ans1 = [True, False, True, True, False, False, False, False, True, False, True, True, False] 

    # reset state variables
    def teardown_method(self, method):
        self.input1 = None

    def test_is_unique_dict(self):
        assert list(map(is_unique_dict, self.input1)) == self.ans1

    def test_is_unique_arr(self):
        assert list(map(is_unique_arr, self.input1)) == self.ans1

    def test_is_unique_bit(self):
        assert list(map(is_unique_bit, self.input1)) == self.ans1


# Check Permutation
class TestCheckPermutation:

    def setup_method(self, method):
        self.input1 = ["amigo?", "12zz!?", "hello1", "", "hey*", 
                       "a", "dogod", "flask", "~1246this", "mil~k"]
        self.input2 = ["go?ima", "z21s.!", "hello", "", "", 
                       "b", "goddo", "flush", "this~1246", "mlk~k"]
        self.ans1 = [True, False, False, True, False, False, True, False, True, False] 

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.ans1 = None

    def test_is_permute_dict(self):
        assert list(map(is_permute_dict, self.input1, self.input2)) == self.ans1

    def test_is_permute_arr(self):
        assert list(map(is_permute_arr, self.input1, self.input2)) == self.ans1


# URLify
class TestReplaceSpaces:

    def setup_method(self, method):
        self.input1 = "Mr  John Smith    "
        # the string in triple quote has difference with different indents
        # remove indent to make sure string equal
        self.input2 = """Mr  John Smith    
Mrs  John Smith     
expression   this   """

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None

    def test_replace_spaces_loop(self):
        assert replace_spaces_expression(self.input1) == "Mr%20John%20Smith"
        assert replace_spaces_expression(self.input2) == """Mr%20John%20Smith%20
Mrs%20John%20Smith%20
expression%20this"""


# Palindrome Permutation
class TestCheckPermutationOfPalindrome:

    def setup_method(self, method):
        self.input1 = ["universal", "tactcoa", "adcocda", "", "abcdefg", "thissiht", "thisasiht", "school"]
        self.ans1 = [False, True, True, True, False, True, True, False]

    def teardown_method(self, method):
        self.input1 = None
        self.ans1 = None

    def test_check_permutation_of_palindrome(self):
        assert list(map(is_permute_palindrome_arr, self.input1)) == self.ans1

    def testIsPermPalinDict(self):
        assert list(map(isPermPalinDict, self.input1)) == self.ans1
# One Away
class TestFindIfOneEditAway:

    def setup_method(self, method):
        self.input1 = ["tech", "tech", "tech", "tech", "tech", 
                       "", "", "", "a", "university", "dog", "tech"]
        self.input2 = ["teach", "ech", "tach", "tech", "team", 
                       "", "e", "ed", "b", "universal", "hog", "aacc"]
        self.ans1 = [True, True, True, True, False, True, True, False, True, False, True, False] 

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.ans1 = None

    def test_find_if_one_edit_away(self):
        assert list(map(oneway_dict, self.input1, self.input2)) == self.ans1

# String Compression
class TestFindStringCompression:

    def setup_method(self, method):
        self.input1 = ["aabcccccaaa", "", "a", "ab", "aaaaapplllllle", "aaaaaaaa"]
        self.ans1 = ["a2b1c5a3", "", "a1", "a1b1", "a5p2l6e1", "a8"]

    def teardown_method(self, method):
        self.input1 = None
        self.ans1 = None

    def test_find_string_compression(self):
        assert list(map(string_compress, self.input1)) == self.ans1

    def testCompreStr(self):
        assert list(map(compreStr, self.input1)) == self.ans1

# Rotate Matrix
class TestRotateMatrix():

    def setup_method(self, method):
        self.input1 = [
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], 
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], 
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]], 
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[]], 
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
            [[5]], 
            [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
        self.input2 = [90, 450, -90, -450, 90, 0, -90, 180, -270]
        self.ans1 = [
            [[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]], 
            [[12, 8, 4, 0], [13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3]], 
            [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]], 
            [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]],
            [[]],
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[5]],
            [[15, 14, 13, 12], [11, 10, 9, 8], [7, 6, 5, 4], [3, 2, 1, 0]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]]]

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.ans1 = None

    def test_rotate_matrix_with_degree(self):
        assert list(map(rotate_matrix_with_degree, self.input1, self.input2)) == self.ans1


# Zero Matrix
class TestZeroMatrix():

    def setup_method(self, method):
        self.input1 = [
            [[1, 2, 3], [4, 0, 6], [7, 8, 9]], 
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [],
            [[1]],
            [[1, 0], [3, 4]],
            [[1, 2], [0, 4]],
            [[1, 2, 3], [4, 5, 6], [7, 0, 9]],
            [[0, 2], [3, 4]],
            [[0]],
            [[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16]],
            [[1, 2, 3, 4], [0, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 16]],
            [[0, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [0, 14, 15, 16]],
            [[1, 2, 3, 0], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]],
            [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 0, 12], [13, 14, 15, 16]],
            [[1, 0, 3], [0, 5, 6], [7, 8, 0]]]
        self.ans1 = [
            [[1, 0, 3], [0, 0, 0], [7, 0, 9]], 
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [],
            [[1]],
            [[0, 0], [3, 0]],
            [[0, 2], [0, 0]],
            [[1, 0, 3], [4, 0, 6], [0, 0, 0]],
            [[0, 0], [0, 4]],
            [[0]],
            [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12], [13, 0, 15, 16]],
            [[1, 2, 0, 4], [5, 6, 0, 8], [9, 10, 0, 12], [0, 0, 0, 0]],
            [[0, 2, 3, 4], [0, 0, 0, 0], [0, 10, 11, 12], [0, 14, 15, 16]],
            [[1, 2, 3, 0], [5, 6, 7, 0], [0, 0, 0, 0], [13, 14, 15, 0]],
            [[0, 0, 0, 0], [0, 6, 7, 8], [0, 10, 11, 12], [0, 14, 15, 16]],
            [[0, 2, 3, 4], [0, 6, 7, 8], [0, 10, 11, 12], [0, 0, 0, 0]],
            [[0, 0, 0, 0], [5, 6, 7, 0], [9, 10, 11, 0], [13, 14, 15, 0]],
            [[1, 2, 3, 0], [5, 6, 7, 0], [9, 10, 11, 0], [0, 0, 0, 0]],
            [[1, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 0], [13, 0, 0, 16]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    def teardown_method(self, method):
        self.input1 = None
        self.ans1 = None

    def test_zero_matrix_inplace(self):
        assert list(map(zero_matrix_inplace, self.input1)) == self.ans1

    def test_zero_matrix_dict(self):
        assert list(map(zero_matrix_dict, self.input1)) == self.ans1


# String Rotation
class TestStringRotation:

    def setup_method(self, method):
        self.input1 = ["waterbottle", "canada", "helloworld", "", "", "hello", "a", "mcmaster", "mcmaster"]
        self.input2 = ["erbottlewat", "canada", "worldlohel", "", "h", "hello", "a", "ermcmast", "masteral"]
        self.ans1 = [True, True, False, True, False, True, True, True, False]

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.ans1 = None

    def test_find_string_compression(self):
        assert list(map(is_rotate_string, self.input1, self.input2)) == self.ans1
