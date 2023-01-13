# # Check Permutation
# 
# Given two strings, write a method to decide if one is a 
# permutation of the other.
#     
# A Permutation of a string: another string that contains same 
# characters, but they can have different orders, only the order 
# of characters can be different. For example, “abcd” and “dabc” 
# are Permutation of each other.
#     
# Please ask interviewer about whether blank spaces or case 
# sensitive need to be considered. "dog" and "god" or "Dog" and "dog"

# check permutation based on two dictionaries
def is_permute_dict(input1, input2):
    dict1 = convToDict(input1, {})
    dict2 = convToDict(input2, {})
    return dict1 == dict2

# convert input to a dictionary
def convToDict(s, dict):
    for ele in s:
        if ele in dict: 
            dict[ele] += 1
        else:
            dict[ele] = 1
    return dict

# check permutation based on two array
def is_permute_arr(input1, input2):
    dict1 = convToArray(input1, [0]*128)
    dict2 = convToArray(input2, [0]*128)
    return dict1 == dict2

# convert input to an array
def convToArray(s, arr):
    for ele in s:
        arr[ord(ele)] += 1
    return arr
