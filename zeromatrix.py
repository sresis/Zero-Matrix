"""Given an NxM matrix, if a cell is zero, set entire row and column to zeroes.

A matrix without zeroes doesn't change:

    >>> zero_matrix([[1, 2 ,3], [4, 5, 6], [7, 8, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

But if there's a zero, zero both that row and column:

    >>> zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]])
    [[0, 0, 0], [4, 0, 6], [7, 0, 9]]

Make sure it works with non-square matrices:

    >>> zero_matrix([[1, 0, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [[0, 0, 0, 0], [5, 0, 7, 8], [9, 0, 11, 12]]
"""


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""
    # go through each item in each list 
    # identify the zero
    # store the location of the zero (in a tuple)
    # get the size of matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    has_zero = False

    # if number is 0, store it
    for x in range(num_rows):
        for y in range(num_cols):
            if matrix[x][y] == 0:
                zero_row = x
                zero_col = y
                has_zero = True
    
    if has_zero is False :
        return matrix
    
    #change it to 0 if it is in the row or column
    for x in range(num_rows):
        for y in range(num_cols):
            if x == zero_row or y == zero_col:
                matrix[x][y] = 0
    
    return matrix




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** TESTS PASSED! YOU'RE DOING GREAT!\n")
