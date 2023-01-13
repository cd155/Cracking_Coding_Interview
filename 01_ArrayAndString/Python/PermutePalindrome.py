# 1.4 Check Palindrome
# 
# Given a string, write a function to check if it is a permutation of 
# a palindrome.
 
# A palindrome is a word or phrase that is the same forwards and 
# backwards.

# A permutation is a rearrangement of letters. The palindrome does not 
# need to be limited to just dictionary words.

from CheckPermutation import convToDict

def is_permute_palindrome_arr(input):
    arr = [0]*128
    for i in range(len(input)):
        ord_num = ord(input[i])
        if arr[ord_num] == 0:
            arr[ord_num] += 1
        elif arr[ord_num] == 1:
            arr[ord_num] -= 1
    if sum(arr) == 0 or sum(arr) == 1:
        return True
    else:
        return False

def isPermPalinDict(s):
    sDict = convToDict(s, {})
    odds = [ele for ele in sDict.values() if odd(ele)] 

    if len(odds) in [0, 1]: 
        return True
    else: 
        return False

def odd(n):
    if n%2 != 0: 
        return True
    else: 
        return False
