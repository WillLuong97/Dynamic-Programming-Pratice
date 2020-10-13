#Python3 implementation of leetcode 139. Word Break 

#Problem statement: 
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
#Dynamic Programming using the bottom up method
def wordBreak(s, wordDict):
    #base case: 
    if not s and not wordDict: 
        return False
    #variable to store the length of the word dict
    n = len(s)


    #dp array to store the boolean value of when an index contain a substring that matches the appropriate 
    #combination in the dictionary
    dp = [False] * (n+1)
    dp[0] = True
    #two pointer to go through the string s
    for i in range(n+1):
        for j in range(i-1, -1, -1): #code optimzation: start from the ending of the word dict and look for the 
            #if the array is not doing the best 
            if(dp[j] and s[j:i] in wordDict):
                dp[i] = True
                break

    return dp[n]

#time complexity: O(n), where n is the length of the string
#space complexity: O(n)

    

#main function to run the program
def main():
    print("TESTING WORD BREAKER...")
    s1 = "leetcode"
    s2 = "applepenapple"
    s3 = "catsandog"
    wordDict_01 = ["leet", "code"]
    wordDict_02 = ["apple", "pen"]
    wordDict_03 = ["cats", "dog", "sand", "and", "cat"]
    print(wordBreak(s1, wordDict_01))
    print(wordBreak(s2, wordDict_02))
    print(wordBreak(s3, wordDict_03))
    print("END OF PROGRAM...")
main()