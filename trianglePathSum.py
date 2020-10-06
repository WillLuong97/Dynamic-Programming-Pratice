#python3 implementation for leetcode problem 120. Triangle Path Sum

#Problem statement: 

'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


'''
#Function to implement the code
#triangle is a 2d array
def minimumTotal(triangle):
    #base case: 
    if not triangle: 
        return 0
    
    #create an array that would store a list of all the sum, the top of the array only has 1 element in it, which makes it the smallest element
    dp = [triangle[0][0]]
    
    #loop throught the outer layer of the triangle 2d array 
    for i in range(1, len(triangle)):
        newDp = [triangle[i][0] + dp[0]] #first element of the row, only one exist
        print(newDp)
        #Loop through the inner array: 
        for j in range(1, i): #add the number that are in the middle of the row, which are bounded by the first and last element of the array.
            newDp.append(min(dp[j], dp[j-1]) + triangle[i][j])
        newDp.append(triangle[i][-1] + dp[-1])
        #override the final db array with the temp newDp array
        dp = newDp
    return min(dp)

#Main function to run the code
def main():
    print("TESTING TRIANGLE PATH...")
    test_array = [[2], [3,4], [6,5,7],[4,1,8,3]]
    print(minimumTotal(test_array))
    

    print("END OF TESTING...")


main()