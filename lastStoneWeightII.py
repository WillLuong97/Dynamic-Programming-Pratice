#Leetcode 1049. Last Stone Weight II

'''
Problem statement: 
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)
Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
Note:
1 <= stones.length <= 30
1 <= stones[i] <= 100
'''
def lastStoneWeightII(stones):
    #base case: 
    if not stones:
        return None
    
    #create a DP array to store all local outcome from the smashing: 
    DP = set()
    DP.add(stones[0])

    #loop through the search space: 
    for i in range(1, len(stones)):
        next_layer = set()
        while DP:
            previous_stone = DP.pop()
            next_layer.add(abs(stones[i] - previous_stone))
            next_layer.add(stones[i] + previous_stone)
        DP = next_layer
    return min(DP)
#Main function to run the program
def main():
    print("TESTING LAST STONE WEIGHT II...")
    #test cases: 
    stones = [2,7,4,1,8,1]
    print(lastStoneWeightII(stones))
    print("END OF TESTING...")

main()