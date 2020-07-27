# Check Substring: 
# Given two strings,write a method to decide if one is a substring of the other.

def check_substring(string_one, string_two):
    if len(string_one) > len(string_two):
        return pair_string(string_one, string_two)
    else:
        return pair_string(string_two, string_one)

def pair_string(string_long, string_short):
    if len(string_short) == 0:
        return False

    for i in range(len(string_long)):
        base = string_long[i:i+len(string_short)]
        if base == string_short:
            return True
    return False

# for test only
test_arrays = [["abbcaaade","aaa"],["",""],["thisis","is"],["","ab"],["a","b"]]
for item in test_arrays:
    if check_substring(item[0],item[1]):
        print(item)
        print("has permutation")
    else:
        print(item)
        print("no permutation")