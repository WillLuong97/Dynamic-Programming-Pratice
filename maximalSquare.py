#Problem 221. Maximal Square

'''
Problem statement: 
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

'''
def maximalSquare(matrix):
    #base case: 
    if not matrix:
        return 0
    #getting the matrix dimension
    m = len(matrix)
    n = len(matrix[0])
    sq_height = 0
    DP = [[0] * (n+1) for _ in range(m+1)]

    #iterate through the martix to calculate the square
    for i in range(1, m+1):
        for j in range(1, n+1):
            #if the current element is equal to 1, perform some necessary computation
            if matrix[i-1][j-1] == '1':
                #add 1 to the minimum square that its neighbor can make,
                DP[i][j] = 1+ min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1])
                sq_height = max(sq_height, DP[i][j])
    #return the area of the squares. 
    return sq_height * sq_height


#Main function to run the test case:
def main():
    print("TESTING MAXIMAL SQUARE...")
    matrix_01 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix_02 = [["0","1"],["1","0"]]
    matrix_03 = [["0"]]

    print(maximalSquare(matrix_01))
    print(maximalSquare(matrix_02))
    print(maximalSquare(matrix_03))
    
    print("END OF TESTING...")
main()