#Problem 1664. Ways to Make a Fair Array
'''
You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.

For example, if nums = [6,1,7,4,1]:

Choosing to remove index 1 results in nums = [6,7,4,1].
Choosing to remove index 2 results in nums = [6,1,4,1].
Choosing to remove index 4 results in nums = [6,1,7,4].
An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.

Return the number of indices that you could choose such that after the removal, nums is fair.

Example 1:

Input: nums = [2,1,6,4]
Output: 1
Explanation:
Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
There is 1 index that you can remove to make nums fair.
Example 2:

Input: nums = [1,1,1]
Output: 3
Explanation: You can remove any index and the remaining array is fair.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: You cannot make a fair array after removing any index.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104

Approach:
We are going to find the sum of all even number and odd number and assign them into two variable: evenSum and oddSUM. 
Then we take turn remove each value out of the orignal list and check if evenSum and oddSum would still be equal to each other. 
If they are both equal to each other, then increment the fair way by 1 and keep going.  
'''
def waysToMakeFair(nums):
	#base case:
	if not nums: 
		return None
	evenSum = 0 
	oddSum = 0
	j = 1	
	# finding the sum of all odd and even number into different values
	while j  < len(nums):
		if j % 2 == 1:
			oddSum += nums[j]

		else: 
			evenSum += nums[j]
		j+= 1
	#result variable 
	count = 1 * (evenSum == oddSum) 
	#loop through the list and take out each value and check if the 
	#even sum and odd sum are still equal 
	i = 1
	while i <len(nums):
		#if i is odd indexed: 
		if i % 2 == 1:
			#remove the index out of the sum and calculate the new sum
			oddSum += nums[i-1] - nums[i]
		else: 
			evenSum += nums[i-1] - nums[i]	
		i += 1 
		count += (oddSum == evenSum)
	return count

'''
Time complexity: O(n), the alogorithm will have to run through all number in the array to find the sum for odd and even and then 
remove one number each to check for ways that the two sum can be equal. 
Space complexity: O(1), we are not storing anything beside the two sum variable.
'''
#Main function to run the test cases: 
def main():
	print("TESTING WAYS TO MAKE A FAIR ARRAY...")
	
	print(waysToMakeFair([2,1,6,4]))
	print(waysToMakeFair([1,1,1]))
	print(waysToMakeFair([1,2,3]))

	print("END OF TESTING...")

main()

