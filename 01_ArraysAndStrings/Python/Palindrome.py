# # Check Palindrome
# 
#     Given a string, write a function to check if it is a permutation of a palindrome.
#     
#     A palindrome is a word or phrase that is the same forwards and backwards.
#     A permutation is a rearrangement of letters. The palindrome does not need to be limited tojust dictionary words.


def is_permute_pd_arr(input):
    arr = [0]*128
    for i in range(len(input)):
        ord_num = ord(input[i])
        if arr[ord_num] == 0:
            arr[ord_num] += 1
        elif arr[ord_num] == 1:
            arr[ord_num] -= 1
        else:
            raise ValueError 
    if sum(arr) == 0 or sum(arr) == 1:
        return True
    else:
        return False
