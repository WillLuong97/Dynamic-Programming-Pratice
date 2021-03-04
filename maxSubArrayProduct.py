#Problem 152. Maximum Product Subarray

#Problem statement: 

'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''
def maxProduct(nums):
    #base case: 
    if not nums: 
        return None

    #create a variable to store the local min, max, and global max
    localMin = localMax = result = nums[0]

    #loop through the rest of the array to find the largest products
    for i in nums[1:]:
        x,y = i*localMin, i*localMax
        #at each iteration, we will keep track of the local max and min
        localMax = max(i, x, y)
        localMin = min(i,x, y)
        #Determining the global max value
        result = max(result, localMax)

    return result

#main function to run the program
def main():
    print("TESTING MAXIMUM SUB-ARRAY PRODUCT...")
    test_input_0 = [2,3,-2,4]
    test_input_1 = [-2,0,-1]
    print(maxProduct(test_input_0))
    print(maxProduct(test_input_1))
    
    print("END OF TESTING...")

main()
