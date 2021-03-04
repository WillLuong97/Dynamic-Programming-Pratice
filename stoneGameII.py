#Problem 1140. Stone Game II
'''
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104
 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104


#Apparoch: Top-down approach by substracting the sum of all stones in the piles held by one player from the total sum of all stones in a pile. 
On the other hand, by minimizing the sum of one player will lead the maximizing sum of the other player. 
- We just need to find the sum of stones that one player picked and then get the other players by substracting. 
'''
from functools import lru_cache
def stoneGameII(piles):
	#base case: 
	suffix_sum = stone_sum(piles)
	
	#recursive function to check for all the sum of stones 
	@lru_cache(None)
	def dfs(pile, M):
		#finding the sum of all stone in a pile by the player
		sum_next_player = suffix_sum[pile]
		#loop through the remaining pile to find the sum of stones
		for next_pile in range(pile + 1, min(pile + 2*M +1,len(piles)+1)):
			sum_next_player = min(sum_next_player, dfs(next_pile,max(next_pile - pile, M))
		#to get the Alice, we substract bob from the actual pile	
		sum_player = suffix_sum[pile] - suffix_sum[sum_next_player]	
		
		return sum_player
			

	return dfs(0,1)	


#Helper method to calculuate the sum of all the stone in a pile
def stone_sum(pile):
	result = [0]
	for stone in reversed(pile):
		result.append(result[-1] + stone)
	result.reverse()
	return result
		

#Main function to run the test case: 
def main():
	print("TESTING STONE GAME II...")

	piles = [2,7,9,4,4]
	print(stoneGameII(piles))
	piles = [1,2,3,4,5,100]
	print(stoneGameII(piles))
	print("END OF TESTING...")

	
main()
