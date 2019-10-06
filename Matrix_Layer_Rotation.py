"""
Matrix Layer Rotation 

Step1: 
    Traverse all the sides/layer of the array, and store it into temp, rotate the temp, and return to the main matrix.
    
Step2:
    Then short the matrix by 2,2 on both the sides, from 5,4 to 3,2 matrix.
    
    Check the matrix 2,2 and 3,2 have some specific rotation patterns. So is 1,1 size matrix.  
    
    Make  condition for the matrix -> (1,1 || 2,2 || 2,3 )

"""

# i -> Row or from m starts, j -> Column, or from n starts


def matrixRotateIP(matrix, m, n, i=0, j=0):
    if (m, n) == (1, 1):
        return matrix
    if (m, n) == (2, 2):
        temp = matrix[i][j]
        matrix[i][j] = matrix[i+1][j]
        matrix[i+1][j] = matrix[i+1][j+1]
        matrix[i+1][j+1] = matrix[i+1][j]
        matrix[i+1][j] = temp
        return matrix
    else:
        temp = matrix[i][j]
        # top
        for a in range(j, n-j-1):
            matrix[i][a] = matrix[i][a+1]
        matrix[i][n-j-1] = matrix[i+1][n-j-1]
        # right
        for a in range(i+1, m-i-2):
            matrix[a][n-1-j] = matrix[a+1][n-1-j]
        matrix[m-j-2][n-j-1] = matrix[m-j-1][n-j-1]
        # bottom
        for a in range(n-j-1, j, -1):
            matrix[m-j-1][a] = matrix[m-j-1][a-1]
        matrix[m-j-1][j] = matrix[m-j-2][j]
        # left
        for a in range(m-i-2, i, -1):
            matrix[a][i] = matrix[a-1][i]
        matrix[i+1][j] = temp
        return matrix


def driverCode(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    i, j = 0, 0
    while (i, j) < (m//2, n//2):
        for _ in range(r):
            s = matrixRotateIP(matrix, m, n, i, j)
        i += 1
        j += 1    
    printMatrix(s)


def printMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    print('\n'.join([' '.join(['{:n}'.format(item) for item in row]) 
      for row in matrix]))
       

# def dirstribute(matrix,m,n):
#     m =


matrix = [[1, 2, 3, 7, 80], [4, 5, 23, 6, 8], [1, 3, 55, 67, 14],
          [7, 89, 56, 17, 20], [23, 123, 85, 10, 414], [13, 34, 58, 45, 56]]

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# out = traversethearray(matrix, 3, 4)
printMatrix(matrix)
# out = matrixRotateIP(matrix, 6, 5, 1, 1)
# out = driverCode(matrix, 3)
print("--"*15)
out = driverCode(matrix, 2)
# printMatrix(out)
# printMatrix(matrix)
# out = driverCode(matrix, 3)
# print(out)
