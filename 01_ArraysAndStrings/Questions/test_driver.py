from pytest import *
from URLify import replace_spaces_expression
from PalindromePermutation import check_permutation_of_palindrome_with_pre_process
from OneAway import find_if_one_edit_away


# URLify
class TestReplaceSpaces:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.test_input1 = "Mr  John Smith    "
        # the string in triple quote has difference with different indents
        # remove indent to make sure string equal
        self.test_input2 = """Mr  John Smith    
Mrs  John Smith     
expression   this   """
        self.test_output1 = "Mr%20John%20Smith"
        self.test_output2 = """Mr%20John%20Smith%20
Mrs%20John%20Smith%20
expression%20this"""

    # reset state variables
    def teardown_method(self, method):
        self.test_input1 = None
        self.test_input2 = None
        self.test_output1 = None
        self.test_output2 = None

    def test_replace_spaces_loop(self):
        assert replace_spaces_expression(self.test_input1) == self.test_output1
        assert replace_spaces_expression(self.test_input2) == self.test_output2


# Palindrome Permutation
class TestCheckPermutationOfPalindrome:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.input1 = "Tact Coa"
        self.input2 = "taco cat"
        self.input3 = "atieo cta"

    # reset state variables
    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.input3 = None

    def test_replace_spaces_loop(self):
        assert check_permutation_of_palindrome_with_pre_process(self.input1)
        assert check_permutation_of_palindrome_with_pre_process(self.input2)
        assert not check_permutation_of_palindrome_with_pre_process(self.input3)


# One Away
class TestFindIfOneEditAway:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.input1 = ["pale", "ple"]
        self.input2 = ["pales", "pale"]
        self.input3 = ["pale", "pale"]
        self.input4 = ["pale", "bake"]
        self.input5 = ["bake", "paleee"]
        self.input6 = ["test111", "test1"]

    # reset state variables
    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.input3 = None
        self.input4 = None
        self.input5 = None
        self.input6 = None

    def test_replace_spaces_loop(self):
        assert find_if_one_edit_away(self.input1[0], self.input1[1])
        assert find_if_one_edit_away(self.input2[0], self.input2[1])
        assert find_if_one_edit_away(self.input3[0], self.input3[1])
        assert not find_if_one_edit_away(self.input4[0], self.input4[1])
        assert not find_if_one_edit_away(self.input5[0], self.input5[1])
        assert not find_if_one_edit_away(self.input6[0], self.input6[1])
