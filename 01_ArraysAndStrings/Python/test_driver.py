from pytest import *
from CheckSubstring import check_substring
from IsUnique import *
from CheckPermutation import *
from URLify import replace_spaces_expression
from PalindromePermutation import check_permutation_of_palindrome_with_pre_process
from OneAway import find_if_one_edit_away
from StringCompression import find_string_compression
from RotateMatrix import rotate_matrix_multiple_times


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
        self.input1 = "abcdee", "cbeeda"
        self.input2 = [["zhc", "zh!"], ["xy", "xyz"]]

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None

    def test_check_permutation_replace(self):
        assert check_permutation_replace(self.input1[0], self.input1[1])
        for e in self.input2:
            assert not check_permutation_replace(e[0], e[1])

    def test_check_permutation_hash(self):
        assert check_permutation_hash(self.input1[0], self.input1[1])
        for e in self.input2:
            assert not check_permutation_hash(e[0], e[1])


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
        self.input1 = "Tact Coa"
        self.input2 = "taco cat"
        self.input3 = "atieo cta"

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.input3 = None

    def test_check_permutation_of_palindrome(self):
        assert check_permutation_of_palindrome_with_pre_process(self.input1)
        assert check_permutation_of_palindrome_with_pre_process(self.input2)
        assert not check_permutation_of_palindrome_with_pre_process(self.input3)


# One Away
class TestFindIfOneEditAway:

    def setup_method(self, method):
        self.input1 = [["pale", "ple"], ["pales", "pale"], ["pale", "pale"]]
        self.input2 = [["pale", "bake"], ["bake", "palee"], ["test111", "test1"], ["hello", "hellwor"]] 

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None

    def test_find_if_one_edit_away(self):
        for e in self.input1:
            assert find_if_one_edit_away(e[0], e[1])
        for e in self.input2:
            assert not find_if_one_edit_away(e[0], e[1])

# String Compression
class TestFindStringCompression:

    def setup_method(self, method):
        self.input1 = "aabcccccaaa"
        self.input2 = "abcd"

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None

    def test_find_string_compression(self):
        assert find_string_compression(self.input1) == "a2b1c5a3"
        assert find_string_compression(self.input2) == "abcd"


# Rotate Matrix
class TestRotateMatrix():

    def setup_method(self, method):
        self.input1 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.input2 = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        self.input3 = [[3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13], [0, 4, 8, 12]]

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.input3 = None

    def test_rotate_matrix_multiple_times(self):
        assert rotate_matrix_multiple_times(self.input1, 4, 630) == self.input3
        assert rotate_matrix_multiple_times(self.input2, 4, -90) == self.input3


# SubString
class TestCheckSubstring():

    def setup_method(self, method):
        self.input1 = "abbcaaade","aaa"
        self.input2 = [["","ab"],["python3","xyz"]]

    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None

    def test_check_substring(self):
        assert check_substring(self.input1[0], self.input1[1])
        for e in self.input2:
            assert not check_substring(e[0], e[1])
