# Check Substring: 
# Given two strings,write a method to decide if one is a substring of the other.

# Solution: Check every substring.
# Assume user put target string first, and substring second


def check_substring(target, sub_str):
    if len(target) == 0 or len(sub_str) == 0:
        return False
    for i in range(len(target)):
        base = target[i:i+len(sub_str)]
        if base == sub_str:
            return True
    return False
