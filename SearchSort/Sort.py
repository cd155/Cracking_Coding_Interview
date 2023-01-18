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
"""

# quick  sort (aka pivot sort)
# merge  sort
# heap   sort

