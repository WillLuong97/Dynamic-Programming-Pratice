#Problem split string with spaces
'''
Given a non-empty string s and dictionary wordDict contatining a list of non-empty words, determine if s can be segmented
into a space-seperated of one or more dictionary words

=> Check if s can be divided into different forms that are also contained in the dictionary
=> Return True or False if there is a valid string

Aproach: Dynamic Programming, store each index whether you can create a space deliminated word, and each time looking back and comparing if at each index can form a word, and if that word 
is also contained in the word dictionary 
Example: 
input = "facebook"`

wordDict = {"face", "book", "facebook"}
n = len(wordDict)
an array with the size len(input), this help give 
[False, False,....] x n => boolean indicating whether if input[:index] can be segmented into a space-seperated sequence of one or more dictionary words

algorithm: input[0:1] => is this a word
0:2 => is this a word
0:3 => is this a word
0:4 => is this a word: yes!
-> Check to see if this word is in the set or not

[True, False, False, False, True, ...]
s[:4] => True
through dp, we want to check if s[4:ind] is in the dictionary
=>solution[ind] = True

At the end return solutions[n], where n is the legnth of the input string. 
'''
def space_seperated(s, wordDict):
	n = len(s)
	can_seperated = [False for _ in range(n+1)]
	can_seperated[0] = True
	#this loop will go forward in the array
	for forward in range(1, n+1):
		#this loop will go backward in the array
		for backward in range(forward - 1, -1, -1):
			if can_seperated[forward] == True:
				break
			if can_seperated[backward]:
				if s[backward:forward] in wordDict:
					can_seperated[forward] = True
	return can_seperated[n]
#Time complexity: O(n^2), two loops to go through the entire array
#Space complexity: O(n), where n is the length of the input string
#Follow up: instead of returning true or false, return all possible sub stringi
'''
Facebook 
=> "face", "book", "facebook"

["face book", "facebook"]

pick a string from i to j and see if that's word, if it is, you add it with some tails value or some head value depends on which way you are traversing

solution = {}

solutions[n+1] = ['']

def solve(ind):
	if ind not in solutions:
		solutions[ind] = []
	return solution[ind]

solve(0)
return solutions[0]
'''


def main():
	print("TESTING SPLIT STRING WITH SPACE...")
	s = "facebook"
	wordDict = set(["face", "bk"])
	print(space_seperated(s, wordDict))
	s = "apple"
	wordDict = set(["aapl", "aaple, e"])	
	print(space_seperated(s, wordDict))
	print("END OF TESTING...")	
			
main()
