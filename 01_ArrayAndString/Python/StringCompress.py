# 1.6 String Compression

# Implement a method to perform basic string compression using the 
# counts of repeated characters. For example, the string "aabcccccaaa" 
# would become "a2b1c5a3".
   
# If the "compressed" string would not become smaller than the original 
# string, your method should return the original string. You can assume 
# the string has only uppercase and lowercase letters (a - z).


# pointer version
def string_compress(input1):
    if len(input1) == 0 :
        return "" 
    
    current = node(input1[0])
    compressed = ""
    for i in range(1, len(input1)):
        runner = input1[i]
        if runner == current.name:
            current.count += 1
        else:
            compressed += current.name
            compressed += str(current.count)
            current = node(runner)
    compressed += current.name
    compressed += str(current.count)
    return compressed

class node:
    def __init__(self, name):
        self.name = name
        self.count = 1

# 1. put the same char in a buffer list, 
# 2. if different ele in, write string, release buffer
# 3. rebuild buffer base on step 1
def compreStr(s):
    newS = ""
    holder = []

    for ele in s:
        print(ele, holder)
        if (len(holder) == 0):
            holder = [ele]
        elif (holder[0] == ele):
            holder.append(ele)
        else:
            newS = newS + holder[0] + str(len(holder))
            holder = [ele]

    if len(holder) != 0:
        newS = newS + holder[0] + str(len(holder))

    return newS
