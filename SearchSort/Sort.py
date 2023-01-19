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
    Radix sort: sort each digits until all digits be sorted

    1. find the length
    2. reformat elements with the length, ex if length = 3, then 1 => 001.
    3. put them in to dictionary, base index incrementally
    4. sort the keys, create a new list
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

"""
    quick sort (aka pivot sort)

    1. select a pivot 
    2. move everything smaller than the pivot to the left 
    3. move everything great than  the pivot to the right 
    4. position pivot(s) in the middle 
    5. repeat steps for its left and right
"""

def quickSort(arr):
    if len(arr) < 2:
        return arr

    mid = int(len(arr)/2)
    newParti = qsHelper(arr,mid)
    left = quickSort(newParti[0])
    right = quickSort(newParti[2])

    return left + newParti[1] + right

# move elements left and right
def qsHelper(arr, mid):
    left = []
    right = []
    med = []

    for i in range(0, len(arr)):
        if arr[i] < arr[mid]:
            left.append(arr[i])
        elif arr[i] > arr[mid]:
            right.append(arr[i])
        else:
            med.append(arr[i])

    return [left,med,right]

# merge  sort
# heap   sort

