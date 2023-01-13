# 1.9 String Rotation

# Assume you have a method isSubstring which checks if one word is a 
# substring of another. 

# Given two strings, sl and s2, write code to check if s2 is a rotation 
# of s1 using only one call to isSubstring.

# For exmaple, "waterbottle" is a rotation of"erbottlewat".


def is_rotate_string(target, compare):
    if len(target) != len(compare):
        return False
    size = len(compare)
    breakpoint = 0
    for i in range(size):
        if not is_substring(target, compare[0:i]):
            # Find non substring, subtrack 1 to point previous substring index
            breakpoint = i - 1
            break
    # size + 1 to cover the last character
    for i in range(breakpoint, size + 1):
        if not is_substring(target, compare[breakpoint:i]):
            return False
    return True

def is_substring(target, compare):
    if len(compare) == 0:
            return True
    for i in range(len(target)):
        base = target[i:i+len(compare)]
        if base == compare:
             return True
    return False
