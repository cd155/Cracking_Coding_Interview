from library import *

""" 
    Bubble sort

    Repeatedly steps through the input list element by element, 
    comparing the current element with the one after it, swapping 
    their values if needed. These passes through the list are 
    repeated until no swaps had to be performed during a pass.
"""

def bufferSort(arr):
    if len(arr) < 2:
        return arr

    while(True):
        oldArr = arr.copy()
        newArr = bsInOnePass(arr)
        if oldArr == newArr:
            break
        else:
            arr = newArr
    return arr

def bsInOnePass(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            buffer = arr[i-1]
            arr[i-1] = arr[i]
            arr[i] = buffer
    return arr

"""
    Radix  sort: sort each digits until all digits be sorted

    1. find the length
    2. reformat elements with the length, 
       ex if length = 3, then 1 => 001.
    3. Put them in to dictionary, base index incrementally
    4. Sort the keys, create a new list
    5. repeat step 3 until length times
"""

# Assume Step 1 and 2 be completed
def radixSortHelper(arr, len):
    for i in reversed(range(0,len)):
        # print(newArr)
        newDic = convToDictBaseIndex(arr,{},i)
        arr = rebuildArr(newDic)
    return arr

# rebuild 
def rebuildArr(dic):
    newArr = []
    sortedKeys = list(dic.keys())
    sortedKeys.sort()
    for key in sortedKeys:
        newArr.extend(dic[key])
    return newArr

# quick  sort (aka pivot sort)
# merge  sort
# heap   sort

