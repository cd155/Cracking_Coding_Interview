# # Check Permutation
# 
#     Given two strings, write a method to decide if one is a permutation of the other.
#     
#     A Permutation of a string: another string that contains same characters, but they can have different orders, only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.
#     
#     Please ask interviewer about whether blank spaces or case sensitive need to be considered. "dog" and "god" or "Dog" and "dog"


def is_permute_dict(input1, input2):
    if len(input1) != len(input2):
        return False
    dict1 = {}
    dict2 = {}
    for i in range(len(input1)):
        if input1[i] in dict1:
            dict1[input1[i]] += 1
        else:
            dict1[input1[i]] = 1
        if input2[i] in dict2:
            dict2[input2[i]] += 1
        else:
            dict2[input2[i]] = 1
    return dict1 == dict2

def is_permute_arr(input1, input2):
    if len(input1) != len(input2):
        return False
    arr1 = [0]*128
    arr2 = [0]*128
    for i in range(len(input1)):
        arr1[ord(input1[i])] += 1
        arr2[ord(input2[i])] += 1
    return arr1 == arr2
