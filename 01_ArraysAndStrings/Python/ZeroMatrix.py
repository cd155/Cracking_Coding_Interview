# # Zero Matrix
#     Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

def zero_matrix_inplace(input1):
    size = len(input1)

    is_first_row_zero = False
    is_first_column_zero = False

    # determin whether first row and first column are zero
    for i in range(0, size):
        if input1[0][i] == 0:
            is_first_row_zero = True
        if input1[i][0] == 0:
            is_first_column_zero = True

    # use first row and first column to store data, there for skip first row and first column
    for i in range(1, size):
        for j in range(1, size):
            if input1[i][j] == 0:
                input1[0][j] = 0
                input1[i][0] = 0

    # update zero base on first row and first column
    for j in range(1, size):
        if input1[0][j] == 0:
            for i in range(1, size):
                input1[i][j] = 0
        if input1[j][0] == 0:
            input1[j] = [0]*size

    # update first row and first column
    if is_first_row_zero:
        input1[0] = [0]*size
    if is_first_column_zero:
        for i in range(0, size):
            input1[i][0] = 0

    return input1


def zero_matrix_dict(input1):
    size = len(input1)
    row_arr = [False]*size
    column_arr = [False]*size

    for i in range(0, size):
        for j in range(0, size):
            if input1[i][j] == 0:
                row_arr[i] = True
                column_arr[j] = True

    for i in range(0, size):
        for j in range(0, size):
            if row_arr[i] or column_arr[j]:
                input1[i][j] = 0                

    return input1
