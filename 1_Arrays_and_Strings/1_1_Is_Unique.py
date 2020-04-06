# Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

test_array = ["algorithm", "", "additional", "h", "2020", "DonaldTrump", "Tt", "12ad好"]

def is_unique_hash(test_string):
    dict_table = {}
    for char in test_string:
        if char in dict_table:
            print ("Hash: Find the duplicate in " + test_string)
            return
        else:
            dict_table[char] = True
    print ("Hash: No duplicate in " + test_string)

def is_unique_array(test_string):
    bool_array = [False] * 128
    for char in test_string:
        if ord(char) > 128:
            print ("Array: Out of Assumption in " + test_string)
            return

        if bool_array[ord(char)]:
            print ("Array: Find the duplicate in " + test_string)
            return
        else:
            bool_array[ord(char)] = True
    print ("Array: No duplicate in " + test_string)

def is_unique_bit_array(test_string):
    # check the following if you have some trouble to understand the bit vector solution
    # https://stackoverflow.com/questions/9141830/explain-the-use-of-a-bit-vector-for-determining-if-all-characters-are-unique
    pass

# for test only
for test_string in test_array:
    is_unique_hash(test_string)
    is_unique_array(test_string)
