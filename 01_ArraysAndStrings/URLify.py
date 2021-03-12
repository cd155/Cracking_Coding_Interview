# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

# EXAMPLE
# Input: "Mr  John Smith    ", 13 
# Output: "Mr%20John%20Smith"

# Solution1: Use regular expression

import re


def replace_spaces_expression(input_string):

    # replace last whitespace to match the exmaple
    match_pattern = '([^ ]*) * $'
    replacement_pattern = r'\g<1>'
    input_string = re.sub(match_pattern, replacement_pattern, input_string)

    # replace all single or more spaces with one %20
    match_pattern = '([^ ]*) +'
    replacement_pattern = r'\g<1>%20'
    return re.sub(match_pattern, replacement_pattern, input_string)

from pytest import *


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
