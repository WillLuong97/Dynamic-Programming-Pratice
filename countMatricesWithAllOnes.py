#Problem 1277. Count Square Submatrices with All Ones
'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
def countSquares(matrix):
	n = len(matrix)
	m = len(matrix[0])
	#create a dp matrix with the same dimension as the orginal matrix to store the number of 1's square
	dp = [[0] * m for _ in range(n)]
	result = 0
	#loop through the original matrix to find the number of cells containing a 1
	for i in range(n):
		for j in range(m):
			#skip if the current cell is  a 0
			if matrix[i][j] == 0:
				continue
			#if the cell is outer layer, so we just add 1 to it, because it cannot branch out and build another square aside from itself
			dp[i][j] = 1
			if i > 0 and j > 0:
				#inner cell, so perform the combining task here
				dp[i][j] += min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
			result += dp[i][j]
	return result

#Time complexity: O(n), where n i every element in the orignal matrix
#Spcae complexity: O(n), we have to create a matrix with with the same size as the original array. 

#Main function to run the test cases
def main():
    print("TESTING COUNT SQUARE SUBMATRICES WITH ALL ONES...")
    #test cases: 
    matrix_01 =[
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ]

    matrix_02 =[
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ]
    print(countSquares(matrix_01))
    print(countSquares(matrix_02))
    print("END OF TESTING..")
main()
