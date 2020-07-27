# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.
# A Permutation of a string:another string that contains same characters, but they can have different orders, 
# only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.

# Please ask interviewer about whether blank spaces or case sensitive need to be considered.
# "dog    " and "    god" or "Dog" and "dog"

# The following examples exclude condtions with blank spaces and case sensitive.
def check_permutation_brutefoce(string_one, string_two):

    if len(string_one) != len(string_two):
        return False

    for char_one in string_one:
        checker = False
        for char_two in string_two:
            if char_one == char_two:
                string_two.replace(char_two, '', 1)
                checker = True
        if not checker:
            return False
    return True


def check_permutation_hash(string_one, string_two):
    dict_table_one = {}
    dict_table_two = {}

    if len(string_one) != len(string_two):
        return False

    # Add string one into dictionary
    for char in string_one:
        if char not in dict_table_one:
            dict_table_one[char] = 1
        else: 
            dict_table_one[char] = dict_table_one[char] + 1
    
    # Add string two into dictionary
    for char in string_two:
        if char not in dict_table_two:
            dict_table_two[char] = 1
        else: 
            dict_table_two[char] = dict_table_two[char] + 1
    
    if len(dict_table_one) != len(dict_table_two):
        return False
    
    for key in dict_table_one:
        if key not in dict_table_two:
            return False

        if dict_table_one[key] != dict_table_two[key]:
            return False
    return True

# for test only
testarrays = [["abcd","cbda"],["","a"],["b",""],["mcmaster","masterma"],["a","b"],["hello", "lhole"],["zc","z!"]]

for testset in testarrays:
    if check_permutation_brutefoce(testset[0], testset[1]):
        print("* " + testset[0] + " is a permutation of " + testset[1])
    else:
        print("* " + testset[0] + " is NOT a permutation of " + testset[1])
    
    if check_permutation_hash(testset[0], testset[1]):
        print("# " + testset[0] + " is a permutation of " + testset[1])
    else:
        print("# " + testset[0] + " is NOT a permutation of " + testset[1])