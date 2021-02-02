#Problem 1043. Partition Array for Maximum Sum

'''
Given an integer array arr, you should partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''

'''
Intuition

The idea is fairly straightforward. We try every combination of i....i + k length sublists we can make, and find the maximum value in that sublist. Then we assume we have filled that sublist with this maximum, and try to dp on another combination. We try every possible combination, caching the result to avoid a timeout.

Implementation

Base case is i overflows the length of the array. We return 0, since we do not contribute to the answer
For every given i value, we try i......k possible sublists
In this loop, we find the current maxmim, and multiply if by the length of the current sublist. This is the best we can do so far.
We dp again from that value, trying to make a sublist from that value. Our j becomes the next recursive i argument.
We take the max for all of these
We add lru_cache to avoid a time out.

'''
from functools import lru_cache
def maxSumAfterPartitioning(arr, k):
	n = len(arr)
	#helper method to loop through all combination of sublist
	#we also have to cache the helper function so that it would run into time out
	@lru_cache(None)
	def recurse(i):
		#base case:
		if i >= n:
			return 0
		
		max_element = 0
		result = 0
		#make sure that all next element is within the array bound
		for j in range(i, min(n, i+k)):
			max_element = max(max_element, arr[j])
			sumOfMaxEle = (j-i+1) * max_element
			local_sum = sumOfMaxEle + recurse(j+1)

			result = max(result, local_sum)
		return result  
			
	

	return recurse(0)
	
#Time complexity: O(n*k), we try every combination of n and k
#Space complexity: O(n), we have to store the recursion stack for each combination and the worst case is that we have to store all element in it. 
#Main function to run the test cases:
def main():
	print("TESTING PARTITION ARRAY FOR MAXIMUM SUM...")
	#test cases: 
	arr_1 = [1,15,7,9,2,5,10]
	k_1 = 3
	arr_2 = [1,4,1,5,7,3,6,1,9,9,3]
	k_2 = 4
	arr_3 = [1]
	k_3 = 1
	print(maxSumAfterPartitioning(arr_1, k_1))
	print(maxSumAfterPartitioning(arr_2, k_2))
	print(maxSumAfterPartitioning(arr_3, k_3))

	print("END OF TESTING...")
main()
