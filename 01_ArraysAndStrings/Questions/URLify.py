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
