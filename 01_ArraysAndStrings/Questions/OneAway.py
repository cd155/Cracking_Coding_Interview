# There are three types of edits that can be performed on strings: insert a character, 
# remove a character, or replace a character. Given two strings, write a function to 
# check if they are one edit (or zero edits) away.
# EXAMPLE:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

# Solution: find the difference between two string, try three methods to alter the first string,
# then match new string with second one. If either one of them (three methods) able to create exact 
# match, return True. Otherwise, return False
# Note: add and remove could reach the same result.

def find_if_one_edit_away(input1, input2):
    length_diff = len(input1) - len(input2)
    if input1 == input2:
        return True
    elif length_diff > 1:
        return False
    elif length_diff < -1:
        return False
    else:
        if length_diff == -1:
            buffer = input1
            input1 = input2
            input2 = buffer
        return check_if_one_edit_away(input1, input2)

def check_if_one_edit_away(long_str, short_str):
    for i in range(len(short_str)):
        if long_str[i] != short_str[i]:
            if len(long_str) == len(short_str):
                # replace a character
                modified_str = long_str[:i] + short_str[i] + long_str[i + 1:]
                return modified_str == short_str
            else:
                # remove a character
                modified_str = long_str[:i] + long_str[i + 1:]
                return modified_str == short_str
    # check the last character in the longer string
    if len(long_str) != len(short_str):
        short_str = short_str + long_str[-1]
    return short_str == long_str
