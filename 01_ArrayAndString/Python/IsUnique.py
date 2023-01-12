# # Is Unique: 
#     Implement an algorithm to determine if a string has all unique characters. 
#     
#     What if you cannot use additional data structures?


def is_unique_dict(inputs):
    arr = []
    for cha in inputs:
        if cha in arr:
            return False
        else:
            arr.append(cha)
    return True

def is_unique_arr(inputs):
    arr = [False]*128
    for cha in inputs:
        if arr[ord(cha)]:
            return False
        else:
            arr[ord(cha)] = True
    return True

def is_unique_bit(inputs):
    checker = 0
    for cha in inputs:
        cha_in_num = ord(cha)-ord(" ")
        if checker & 1 << cha_in_num:
            return False
        else: 
            checker |= 1 << cha_in_num
    return True  
