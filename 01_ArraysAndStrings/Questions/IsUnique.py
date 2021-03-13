# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

# Solution1: You can use a hash table to track all characters
# Solution2: Without data structure, you can array to track all characters.
# a character is a unicode, and it could be casted as an interger.
# Read ascii information:
# https://www.ascii-code.com
# Read use bit vector to determine character is unique
# https://stackoverflow.com/questions/9141830/explain-the-use-of-a-bit-vector-for-determining-if-all-characters-are-unique

def is_unique_hash(input1):
    dict_table = {}
    for s in input1:
        if s in dict_table:
            return False
        else:
            dict_table[s] = True
    return True

def is_unique_array(input1):
    bool_array = [False] * 128
    for s in input1:
        if bool_array[ord(s)]:
            return False
        else:
            bool_array[ord(s)] = True
    return True
