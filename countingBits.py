#Prolem 338 Couting bits

'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
#The idea is to use Dynamic programming (bottom-up) approach to reference the value of the already computed value for the current 
#decimal
#If the decimal is odd, the number of 1s that decimal has is referenced by its closest+immediate even number and add 1 extra bit to it. if the number is even, then we just referenced the closest even decimal that it  can get down to
def countBits(num):
	#base case: (using built in bin() function)
#	if not num:
#		return [0]
#	result = []
#	for i in range(num+1):
#		result.append(bin(i).count("1"))

#	return result
	#base case: 
	if not num:
		return[0]
	result = [0]

	for i in range(1, num+1):
		#if the decimal is odd: 
		if i % 2 == 1:
			result.append(result[int(i/2)] +1)

		else:
			result.append(result[int(i/2)])
	return result

#Time complexity: O(n), the algorithm has to run through the entire array to calculate the build the result DP array.
#Space complexity: O(1), we are not making extra spcaes for anything
	
#Main function to run the test cases:
def main():
	print("TESTING COUNTING BITS...")
	
	#Test cases: 
	num_01 = 2
	num_02 = 5	

	print(countBits(num_01))
	print(countBits(num_02))

	print("END OF TESTING...")
main()
