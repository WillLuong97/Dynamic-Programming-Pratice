#Python3 program to implement a solution to find a mninum path sum I and falling minimum path sum

#Minium path sum: 
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
#Dynamic Approach:
def minPathSum(grid):
    #base case: no grid, no output
    if not grid: 
        return 0
    
    #add the sum for outer column and row: 
    for i in range(1, len(grid)):
        grid[i][0] += grid[i-1][0] 

    for j in range(1, len(grid[0])):
        grid[0][j] += grid[0][j-1] 
    #loop through the grid and calculate the sum path: 
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            #calculate the path sum by adding the smaller element into it
            grid[i][j] += min(grid[i - 1][j], grid[i][j-1])
    return grid[-1][-1]

#Falling minimum path sum: 
'''
931. Minimum Falling Path Sum
Medium

913

71

Add to List

Share
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.
Constraints:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100

'''
#Dynamic programming - Memo approach:
def minFallingPathSum(A):
    #base case: no grid, no result
    if not A: 
        return 0
    dp = [[float('inf') for _ in range(len(A[0])+2)] for _ in range(len(A))]
    #loop through the grid to find the minimum falling sum
    for i in range(len(A)): #Row
        for j in range(1, len(A[0])+ 1): #column
            if i == 0: #the first row
                dp[i][j] = A[i][j-1]

            else: 
                dp[i][j] = A[i][j-1] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])

    return min(dp[-1])




#Main function to test the solutions
def main():
    print("TESTING FIND MINIMUM PATH SUM...")
    test_list_01 = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(minPathSum(test_list_01))
    print("TESTING FIND FALLING MINIMUM PATH SUM...")
    test_list02 = [[1,2,3],[4,5,6],[7,8,9]]
    print(minFallingPathSum(test_list02))
    print("END OF PROGRAM... ")
main()