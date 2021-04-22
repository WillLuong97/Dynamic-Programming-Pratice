#Problem 322. Coin Change

'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

'''
def coinChange(coins, amount):
	#base case: 
	if not coins and not amount:
		return 0
	if not coins or not amount:
		return 0
	dp = [amount + 1] * (amount + 1)
	dp[0] = 0
	sortedCoins = sorted(coins)
	#loop through the amount to find the coins
	for i in range(1, amount + 1):
		#loop through the number of ways that can build the coins, but prioritze smaller ways first
		for j in range(len(sortedCoins)):
			if sortedCoins[j] <= i:
				dp[i] = min(dp[i], dp[i-sortedCoins[j]] + 1)
			else:
				break
	return dp[amount] if dp[amount] != amount + 1 else -1
	



#Main function to run the test case: 
def main():
	print("TESTING COIN CHANGE....")
	coins = [1,2,5]
	amount = 11
	print(coinChange(coins, amount))
	coins = [2]
	amount = 3
	print(coinChange(coins, amount))
	coins = [1]
	amount = 0
	print(coinChange(coins, amount))
	coins = [1]
	amount = 1
	print(coinChange(coins, amount))
	coins = [1]
	amount = 2
	print(coinChange(coins, amount))
	

	print("END OF TESTING...")
	
main()
