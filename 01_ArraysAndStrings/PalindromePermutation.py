# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited tojust dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

# Solution: We can use an array whether it is a permutation of palindrome.
# Note: Lower case and upper case do matter in this case.


def check_permutation_of_palindrome(input):
    a = [0] * 128

    for char in input:
        ind = ord(char)
        if a[ind] > 0:
            a[ind] -= 1
        else:
            a[ind] += 1

    f = lambda x: x > 0
    a_gt_one = [char for char in input if f(char)]
    if len(a_gt_one) > 1:
        return False
    else:
        return True


from pytest import *


class TestCheckPermutationOfPalindrome:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.input1 = "Tact Coa"
        self.input2 = "taco cat"
        self.input3 = "atco cta"


    # reset state variables
    def teardown_method(self, method):
        self.input1 = None
        self.input2 = None
        self.input3 = None

    def test_replace_spaces_loop(self):
        assert check_permutation_of_palindrome(self.input1)
        assert check_permutation_of_palindrome(self.input2)
        assert check_permutation_of_palindrome(self.input3)
