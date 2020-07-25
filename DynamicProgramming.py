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

#main function to execute the array: 
# def main():
#     print("**Function to test the Fibonacci number ***")
#     print("**Approach 1: With Recursion")
#     x = 1 
#     y = 2
#     z = 35

#     print(find_fibonacci_RECURSION(x))
#     print(find_fibonacci_RECURSION(y))
#     print(find_fibonacci_RECURSION(z))


#     print("**Approach 2: With Memoization")
#     print(fib_memo(x))
#     print(fib_memo(y))
#     print(fib_memo(z))

#     print("**Approach 3: With Bottom Up")
#     print(find_fibonacci_BOTTOM_UP(x))
#     print(find_fibonacci_BOTTOM_UP(y))
#     print(find_fibonacci_BOTTOM_UP(z))

# main()



