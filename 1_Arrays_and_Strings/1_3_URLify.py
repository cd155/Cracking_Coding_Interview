# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

# EXAMPLE
# Input: "Mr  John Smith    ", 13 
# Output: "Mr%20John%20Smith"

import re

def replace_spaces_expression(input_string):

    # replace last whitespace to match the exmaple
    match_pattern = '([^ ]*) * $'
    replacement_pattern = '\g<1>'
    input_string = re.sub(match_pattern, replacement_pattern, input_string)

    # replace all single or more spaces with one %20
    match_pattern = '([^ ]*) +'
    replacement_pattern = '\g<1>%20'
    return re.sub(match_pattern, replacement_pattern, input_string)

from pytest import *

class TestReplaceSpaces:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.test_input = "Mr  John Smith    " 
        self.test_output = "Mr%20John%20Smith"

    # reset state variables
    def teardown_method(self, method):
        self.test_input = None
        self.test_output = None

    def test_replace_spaces_loop(self):
        assert replace_spaces_expression(self.test_input) == self.test_output

# test_input = "Mr  John Smith    " 
# match_pattern = '([^ ]*) * $'
# replacement_pattern = '\g<1>'
# result1 = re.sub(match_pattern, replacement_pattern, test_input)
# match_pattern = '([^ ]*) +'
# result2 = re.sub(match_pattern, replacement_pattern, result1)
# print(result1)
# print(result2)
