# # One Edit Away 
# 
# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character. 
#     
# Given two strings, write a function to check if they are one edit 
# (or zero edits) away.

from CheckPermutation import convToDict

# give two string, return a bool
def oneway_dict(s1, s2):
    ysValue = updateYsDict(s2, convToDict(s1, {}))
    oneEdits = [ele for ele in ysValue if ele in [1,-1]]

    if (any([ele for ele in ysValue if ele<-1])) or \
       (any([ele for ele in ysValue if ele>1])):
        return False
    elif (len(oneEdits) > 2):
        return False
    elif (sum(ysValue) in [0,1,-1]):
        return True
    else:
        return False

# give a string, return updated dict.values()
def updateYsDict(s, dict):
    for ele in s:
        if ele in dict:
            dict[ele] -= 1
        else:
            dict[ele] = -1
    return (dict.values())
