#Leetcode 213. House Robber II

#Problem statement: 
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
'''
#Function to solve the problem 
#Dynamic Progamming (Bottom-Up approach): Create a decision DP array based on the sub problem conditions
def rob(nums):
    #base case: 
    if not nums: 
        return [0]
    #if there are only two houses, then we can only rob one house without being alert, so just rob the one with the most money
    if len(nums) == 2:
        return max(nums)
    #if there is only one house, then just steal it
    if len(nums) == 1: 
        return nums[0]

    #Helper method to find the house to rob
    def helper(nums):
        #DP array to store the sum of money after each robbery
        DP = [0] * len(nums)
        #buid the DP array
        #base case to build the DP array
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])

        #loop through the rest of the array to find house to rob
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-1], nums[i] + DP[i-2])
        
        return DP[-1]

    #recursively call the function to find which house to rob but we will try to exclude the first and last house
    return max(helper(nums[:-1]), helper(nums[1:]))

#Time complexity: O(n), where n is the number of all element in the house array
#Space complexity: O(n), recursion stack will have to run through all element in the house array

#Main function to test the program
def main():
    print("TESTING HOUSE ROBBER II...")
    #value to test: 
    test_nums_1 = [2,3,2]
    test_nums_2 = [1,2,3,1]
    test_nums_3 = [0]
    print(rob(test_nums_1))
    print(rob(test_nums_2))
    print(rob(test_nums_3))
    print("END OF TESTING...")
main()