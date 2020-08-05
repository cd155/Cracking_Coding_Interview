# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

# EXAMPLE
# Input: "Mr  John Smith    ", 13 
# Output: "Mr%20John%20Smith"

def replace_spaces(test_string):
    has_space = False

    for char in test_string:
        if char == " " and has_space:
            has_space = True
            test_string.replace(" ", "%20", 1)
        else:
            has_space = False
    return test_string