#279. Perfect Squares

'''
Problem statement: 
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import math
#function to find the perfect squares
#Approach: Dynamic programming using bottom up
def numSquares(n):
    #base case: 
    if not n:
        return None
    #create a dp array to store al sub problem
    dp = [float('inf') for _ in range(n+1)] 
    dp[0] = 0
    #loop through the search space to find the least number of squares
    #needed to sum up to n
    for i in range(1, n+1):
        #calculate the least amount of perfect squares to sum up to the current number
        for j in range(1, math.floor(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], 1 + dp[i - j**2])

    return dp[-1]

#main function to run the program
def main():
    print("TESTING PERFECT SQUARES...")
    n_01 = 12
    n_02 = 13
    print(numSquares(n_01))
    print(numSquares(n_02))
    print("END OF TESTING...")
main()