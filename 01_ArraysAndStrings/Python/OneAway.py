# # One Edit Away 
# 
#     There are three types of edits that can be performed on strings: 
#     
#     insert a character, remove a character, or replace a character. 
#     
#     Given two strings, write a function to check if they are one edit (or zero edits) away.


def oneway_dict(input1, input2):
    inorder_arr = inputs_inorder(input1, input2)
    long_input = inorder_arr[0]
    short_input = inorder_arr[1]
    
    arr_dict = [0]*128
    
    for char in long_input:
        char_num = ord(char)
        arr_dict[char_num] += 1
    
    for char in short_input:
        char_num = ord(char)
        arr_dict[char_num] -= 1
    
    edit_arr = [item for item in arr_dict if item != 0]
        
    if len(edit_arr) == 0:
        return True
    elif len(edit_arr) == 1 and edit_arr[0] == 1:
        return True
    elif len(edit_arr) == 2 and -1 in edit_arr and 1 in edit_arr:
        return True
    else:
        return False

def inputs_inorder(input1, input2):
    inorder_arr = []
    if len(input1) > len(input2):
        inorder_arr.append(input1)
        inorder_arr.append(input2)
    else:
        inorder_arr.append(input2)
        inorder_arr.append(input1)
    return inorder_arr
