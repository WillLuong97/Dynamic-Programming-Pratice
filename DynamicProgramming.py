#Python program to test out Dynamic Programming approach through various problems

#Problem #1: Write a function that would take a non-negative integer and return the fibonacci number based at that interger index.
#Fibonnacci sequence = 1, 1, 2, 3, 5, 6, 13, 21,...
# Form = (i - 1) (i - 2)

#Example: fib(3) => 2
        #fib(2) => 1
        #fib(8) => 21

#Approach 1: Use recursion
        
def find_fibonacci_RECURSION(n):
    retNumber = 0
    if n == 1 or n == 2:
        retNumber = 1
    #calling the function recursively to iterate to the fibonacci at n-th 
    else: 
        retNumber = find_fibonacci_RECURSION(n - 1) + find_fibonacci_RECURSION(n-2)
    
    return retNumber
    
memo = []
#Approach 2: Use Memoization 
def find_fibonacci_MEMOIZE(n, memo):
    retNumber = 0
    #An array to store the fib number that has alreadt been calculated 
    if memo[n] is not None:
        #return the fib number being stored in this array
        retNumber = memo[n]
    if n == 1 or n == 2:
        retNumber = 1
    
    else:
        retNumber = find_fibonacci_MEMOIZE(n - 1, memo) + find_fibonacci_MEMOIZE(n - 2, memo)
    #if not, we will add the fib number into the memo
    memo[n] = retNumber
    return retNumber

def fib_memo(n):
    memo = [None] * (n + 1)
    return find_fibonacci_MEMOIZE(n, memo)

#Approach 3: Bottom-up
def find_fibonacci_BOTTOM_UP(n):
    if n == 1 or n == 2: 
        return 1
    #we will construct the array and populate the fib number as we work through them
    bottom_up = [None] * (n + 1)
    #the first two position will 1
    bottom_up[1] = 1
    bottom_up[2] = 1
    #populate the rest of the array with the fib number
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i -1] + bottom_up[i - 2]

    return bottom_up[n]



#LEETCODE #62: Unique Path: 
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Input: m = 7, n = 3
# Output: 28

#Approach 1: using recursion
def uniquePath_RECURSION(m: int, n: int) -> int:
    return total_unique_path(m - 1, n-1)


#Helper method to contain the total unique path:
def total_unique_path(m: int, n:int) -> int:
    #if there is only one way to get to the current spot
    if (m == 0 and n == 0):
        return 1
    
    #invalid path
    if (m < 0 or n <0):
        return 0
    
    #final path: 
    return total_unique_path(m-1, n) + total_unique_path(m, n - 1)

    
# #Approach 2: Using Memoization: 
# def uniquePath_MEMOIZAITON(m: int, n: int) -> int:
#     #dictionary to store the already computed recursive value
#     repeated_val_dict = {}

#     return total_unique_path(m - 1, n - 1, repeated_val_dict)


# #Helper method 2 to contain the total unique path with a dictionary to store repeated values
# def total_unique_path_MEMOIZATION(m, n, repeated_dict):

#     if (m == 0 and n == 0):
#         return 1

#     #Invalid path: 
#     if(m < 0 or n < 0):
#         return 0

#     #checking if m and n has already been computed
#     if (repeated_dict[m] == n):
#         return repeated_dict[m]

#     return repeated_dict 

#Approach 3: Using Bottom up method
def uniquePath_BottomUp(m: int, n: int) -> int:
    #create a two day array to store the values
    calculated_path_array = [[0 for x in range(m + 1)] for y in range(n + 1)]
   
    #Loop through the 2d array and add the calculated path into it:
    for i in range(len(calculated_path_array)):
        for j in range(len(calculated_path_array[i])):
            #if there are only one way to get to a spot on the graph
            if (i == 0 or j == 0):
                calculated_path_array[i][j] = 1
            else:
                calculated_path_array[i][j] = calculated_path_array[i-1][j] + calculated_path_array[i][j-1]
               
    
    #return the last element in the 2d array to see how many path to get to it.
    return calculated_path_array[m-1][n-1]


#UGLY NUMBERS:
# Bruteforce approach:  Loop for all positive integers until the ugly number count is smaller than n, if an integer is ugly than increment ugly integer number count
#To check if a number is ugly, divide the number by greatest divisible powers of 2, 3 and 5, if the number becomes 1 then it is an ugly number otherwise not.
#This approach is taking too much time to compute but the space complexity is O(1)
#Helper method to divide the number by a the prime greatest divisible power of b:
def maxDivides(a,b):
    if(a % b == 0):
        a = a / b

    return a #this should return 1 if the number is ugly
    
#function to check if the number being passed in is ugly or not
def isUglyNumeber(a):
    if((maxDivides(a, 2) == 1) and ((maxDivides(a, 3) == 1) and (maxDivides(a, 5)) == 1)):
        return True

    return False

def uglyNumber_BRUTEFORCE(n):
    i = 1
    uglyNumberCounter = 1
    while n > uglyNumberCounter:
        i += 1
        if(isUglyNumeber(i)):
            uglyNumberCounter += 1

    return uglyNumberCounter
        
    

#Approach 2: Dynamic Programming
# Time complexity: O(n) 
# Space complexity: O(n)
def uglyNumber_TOPDOWN(n):
    #create an array that would store all the ugly number element
    #base case
    ugly_array = [0] * n #intialize the new array with the same size as n
    ugly_array[0] = 1
    i2 = i3 = i5 = 0
    next_multiple_2 = 2
    next_multipl_3 = 3
    next_multiple_5 = 5
 
    #loop through the array to find any ugly number created by 2, 3 or 5
    for i in range(1, n):
        #choose the min values of all the available multiples
        ugly_array[i] = min(next_multiple_2, next_multipl_3, next_multiple_5)
        #increment the value of all the available multiples
        if ugly_array[i] == next_multiple_2:
            i2 += 1
            next_multiple_2 = 2 * ugly_array[i2]

        if(ugly_array[i] == next_multipl_3):
            i3 += 1
            next_multipl_3 = 3 * ugly_array[i3]

        if(ugly_array[i] == next_multiple_5):
            i5 += 1
            next_multiple_5 = 5 * ugly_array[i5]

    #return the last element in the ugly number array
    return ugly_array[-1]



'''
Leetcode 91: Decode ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


'''
def numDecoding(s):
    return helper(s)


#This function will return the integer values of th
def validNum(word):
    return 1 <= int(word) <= 26

#helper fucnction to recurse the algorithm: 
def helper(word):
    #base case:
    if word and word[0] == "0":
        return 0

    if len(word) == 1:
        return 1 if validNum(word) else 0

    if len(word) == 2: 
        if validNum(word):
            return 2 if word[1] != 0 else 0

        return 1 if word[1] != 0 else 0 #we currently do not have the element to represent a 0
    res = 0
    if validNum(word[:2]):
        res = helper(word[2:])

    return res + helper(word[1:])

    





# #main function to execute the function: 
def main():
    # print("**Testing out Unique_path with recursion**")
    # m = 3
    # n = 2
    # print(uniquePath_RECURSION(m, n))
    # print(uniquePath_RECURSION(7, 3))
    # print("**Testing out Bottom_UP method")
    # print(uniquePath_BottomUp(m, n))
    # print(uniquePath_BottomUp(7, 3))
    # print(uniquePath_BottomUp(7,4))

    # print("***Testing the Ugly Numbers***")
    # n = 14
    # print("The ugly number at the nth element is: ")
    # print(uglyNumber_TOPDOWN(n))

    #Testing number of ways to decode 
    test_1 = "12"
    test_2 = "226"
    

    print("TESTING DECODE WAYS...")
    print(numDecoding(test_1))
    print(numDecoding(test_2))

    print("END OF PROGRAM...")


main()



