# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

# Solution: Matrix rotate has its pattern. To take 4 by 4 matrix as an example. n is size
# (0,0) → (0,3) → (3,3) → (3,0) → (0,0)
# (0,1) → (1,3) → (3,2) → (2,0) → (0,1)
# (0,2) → (2,3) → (3,1) → (1,0) → (0,2)
# (x,y) → (y,n-x) → (n-x,n-y) → (n-y,n-(n-x)=x) → (x,n-(n-y)=y)
# Base on the pattern, we rotate matrix row by row. 
# Note1: We only need to go size/2 rows to accomplish the task.
# Note2: We don't need to iterate to last column becasue the first element will be relocated to here.
# Note3: When we move to the next row, we have to reduce the row iterated times, the outter ring already complete 
# some works for you, so don't repeat them.


def rotate_matrix_multiple_times(array2d, size, degree):
    reduce_degree = abs(degree)%360
    rotate_time = 0
    if degree >= 0:
        rotate_time = reduce_degree/90
    else:
        rotate_time = 4 - reduce_degree/90

    for _ in range(int(rotate_time)):
        rotate_matrix_clockwise(array2d, size)
    return array2d

def rotate_matrix_clockwise(array2d, size):
    start = 0 
    end = size -1
    for i in range(int(size/2)):
        # each row iterate size - 1 times
        for j in range(start, end):
            x = j
            y = size-1-i
            current = array2d[i][j]
            next = None
            for _ in range(4):
                next = array2d[x][y]
                array2d[x][y] = current
                buffer = x
                x = y
                y = size-1-buffer
                current = next
        # reduce the next array iterated times
        start += 1
        end -= 1
    return array2d
