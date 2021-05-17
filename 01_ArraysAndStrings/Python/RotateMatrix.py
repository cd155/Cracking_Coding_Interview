# # Rotate Matrix
# 
#     Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# 
# ### Assumption
#     default at clockwise, negative degrees are allowed, negative means counter-clockwise


def rotate_matrix(input1):
    size = len(input1)

    # initialize the outer ring size
    outer_top = 0
    outer_bottom = size - 1

    # iterate size/2 times
    for i in range(0, int(size/2)):

        # iterate times base on the outer ring
        for j in range(outer_top, outer_bottom):
            x = i
            y = j
            buffer = input1[x][y]
            for _ in range(0, 4):
                previous_x = x
                x = y
                y = size-1-previous_x
                
                # swap values
                temp = input1[x][y]
                input1[x][y] = buffer
                buffer = temp

        outer_top += 1
        outer_bottom -= 1

    return input1

def rotate_matrix_with_degree(matrix, degree):
    reduced_degree = abs(degree)%360
    times = 0
    if degree < 0:
        times = 4 - reduced_degree/90
    else:
        times = reduced_degree/90

    for _ in range(0, int(times)):
        rotate_matrix(matrix)

    return matrix
