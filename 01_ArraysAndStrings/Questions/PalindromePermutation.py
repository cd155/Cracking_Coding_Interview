# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited tojust dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

# Solution: We can use an array whether it is a permutation of palindrome.
# Note: Lower or upper case and white space do matter in this case, so make sure ask interviewers.


def check_permutation_of_palindrome(input1):
    a = [0] * 128
    for s in input1:
        ind = ord(s)
        if a[ind] > 0:
            a[ind] -= 1
        else:
            a[ind] += 1

    f = lambda x: x > 0
    a_gt_zero = [e for e in a if f(e)]
    if len(a_gt_zero) > 1:
        return False
    else:
        return True

def pre_process(input1):
    return input1.lower().replace(" ", "")

def check_permutation_of_palindrome_with_pre_process(input1):
    return check_permutation_of_palindrome(pre_process(input1))
