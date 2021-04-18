# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.
# A Permutation of a string:another string that contains same characters, but they can have different orders, 
# only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.
# Please ask interviewer about whether blank spaces or case sensitive need to be considered.
# "dog" and "god" or "Dog" and "dog"
# The following examples exclude condtions with blank spaces and case sensitive.

# Solution: ideally we can use a hash table to track permutation of a string


def check_permutation_replace(input1, input2):
    if len(input1) != len(input2):
        return False
    for s1 in input1:
        print(input2, s1)
        input2 = input2.replace(s1, "", 1)
    return len(input2) == 0

def check_permutation_hash(input1, input2):
    a = [0] * 128
    for s in input1:
        a[ord(s)] += 1
    for s in input2:
        a[ord(s)] -= 1

    f = lambda x: x != 0
    a_not_zero = [e for e in a if f(e)]

    if(len(a_not_zero) == 0):
        return True
    else:
        return False
