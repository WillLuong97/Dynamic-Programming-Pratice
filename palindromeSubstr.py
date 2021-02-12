#647. Palindromic Substrings

'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
'''

#Dynamic Programming Approach: 
'''
Optimal substructure: Remember that larger palindromes are made of smaller palindromes. Congratulation, we have discovered a substructure to our problem! Knowing that a string is made up of a palindrome helps us determine if the string itself is a palindrome.

Here's an example: for the string "axbobxa", the first and the last characters match, so it's a potential palindrome. If we knew already that its substring "xbobx" is also a palindrome, there wouldn't be a need for any further checks.

Overlapping sub-problems: While checking all substrings of a large string for palindromicity, we might need to check some smaller substrings for the same, repeatedly. If we store the result of processing those smaller substrings, we can reuse those while processing larger substrings.

Here's an example: for the string "axbobxa", the substring "bob" needs to checked for the substring "xbobx" and the string "axbobxa". In fact, to check all three of these strings, the single character string "o" needs to be checked.
'''
def countSubstrings(s):
	#base case: 
	if not s:
		return None 
	n = len(s)
	#DP matrix to store the substring that are palindrome that we have found from the previous dp and use them to check for the next element
	dp = [[False]*n for _ in range(n)]
	result = 0
	#start looking through the string
	#We go backward because DP{i][j] depends on DP[i+1][j], so it would be more optimzed to check for the bigger i first and use it to keep track for further
	for i in reversed(range(n)):
		for j in range(i, n):
			#base case: substring of size 1 would always be the palindrome
			if j - i < 2 and s[i] == s[j]:
				dp[i][j] = True
				result += 1
			#for any substring that are larger then 1, then we use the result we found from the substring of size 1 and calculate for the next instance
			elif dp[i+1][j-1] and s[i] == s[j]:
				dp[i][j] = True
				result += 1
	return result
	
#Main function to run the test cases: 
def main():
	print("TESTING PALINDROMIC SUBSTRING...")
	s = "abc"
	print(countSubstrings(s))
	s = "aaa"
	print(countSubstrings(s))
	print("END OF TESTING...")

main()
