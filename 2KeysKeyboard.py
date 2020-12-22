#Leetcode 650. 2 Keys Keyboard

#Problem statement: 
'''
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
'''
#Algoritm: #DP appraoch + Prime factorization
def minSteps(n):
    
    # create a dp array to store the number of steps to copy and paste
    #The index of the db represent the number of A that we must copy and paste
    DP = [float('inf')] * 1001
    #base case: if there is only 1 A, then we dont need to do anything
    DP[1] = 0
    #loop through the possible ways that we can copy and paste
    for x in range(n+1): 
        #loop through the actual number of A that we need to copy and past
        for y in range(1, n):
            if x % y == 0: 
                DP[x] = min(DP[x], x//y + DP[y])

    return DP[n]    


#Prime factorization approach: we treat each of number of A like a factorization of nA
def minSteps_PRIME(n):
    answer = 0
    factorization = 2
    #if n == 1, the smallest way to make A, is 0
    while n > 1: 
        while n % factorization == 0:
            answer += factorization
            n /= factorization
        factorization += 1

    return answer


#main function to test the prgram: 
def main():
    print("TESTING 2 KEYS KEYBOARD...")
    input_01 = 3
    print(minSteps(input_01))
    print(minSteps_PRIME(input_01))
    print("END OF TESTING...")
main()
