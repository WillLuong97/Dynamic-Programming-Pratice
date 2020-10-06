#Python3 implementation of Dynamic Programming pattern in different problems

#Leetcode 746: Min cost climbing stairs 
#Problem statement
'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
#Time complexity: 
O(n) where n is the length of the cost
O(1) the space complexity is used by 1 and 2 
'''
def minCostClimbingStairs(cost):
    #base case: 
    if not cost:
        return None

    #two poiter: 
    p1 = 0
    p2 = 0
    #loop through each cost
    for i in reversed(cost): 
        #swap the element: 
        p1, p2 = i + min(p1, p2), p1
        
    return min(p1, p2)


#***********************LEETCODE 64. Minimum Path Sum***************************
'''
Problem statement: 
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
#Time complexity: O(mxn) where m and n are the dimesion of the given grid
#Space complexity:  O(1) we only work the given grid, thus, not needing any extra spaces.
def minPathSum(grid):
    #base case: 
    if not grid: 
        return None
    #extract the number of row and column of the grid
    numOfRow = len(grid[0])
    numOfcolumn = len(grid)
    
    #calculate the sum of the outer column
    for i in range(1, numOfcolumn):
        grid[i][0] += grid[i-1][0]

    for j in range(1, numOfRow):
        grid[0][j] += grid[0][j-1]

    #the total sum of the rest of the matrix as we loop through them
    #internal node
    for i in range(1, numOfcolumn):
        for j in range(1, numOfRow):
            grid[i][j] += min(grid[i][j-1], grid[i-1][j])

    return grid[-1][-1]

#main function to excute different implementation
def main():
    print("TESTING MIN COST CLIMBING STAIRS...")
    testCost = [10, 15, 20]
    testCost01 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(testCost))
    print(minCostClimbingStairs(testCost01))

    print("END OF TESTING...")

    print("")
    print("TESTING MINIMUN PATH SUM...")
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    print(minPathSum(grid))
    print("END OF TESTING...")

    print("")

main()