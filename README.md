# Dynamic Programming

## Definition:

- In genearal, algorithm is an optimziation over plain recusion. The ided is to simply store the result of subproblems, so that we do not have to recompute them when needed later.



## How to solve a Dynamic Programming Problem: 
- Dynamic Programming (DP) aims to solve problem on polynomial time (n^k) from exponential time (2^n, etc.)

### Steps to solve a DP: 
1. Check if it is a DP problem 
2. Decide a state expression with least parameters 
3. Formulate state relationship
4. Do tabulation (or add memoization)

### Tips and tricks to solve a Dynamic Programming Problem: 
1. Start with a recursive backtracking solution 
2. Optimize it by using a memoization table (top-down dynamic programming)
3. Remove the need for a recursion (bottom-up dynamic programming)
4. Apply final tricks to reduce the time/memorary complexity


+ Step 1: How to determine if a problem is a Dynamic Progarmming Problem? 
    - Problems that require maximize and minimize certain quantity or counting problems that ask to count the arrangement 
    under some condition or certain probability problem
    - All dynamic programming satisfy the overlapping subproblems and optimal substructure property.

+ Step 2: Deciding the state: 
    - DP is all about state and its transition
    - State: is a set of parameters that can uniquely identify a certain position or standing in the given problem. This set of parameters should be as small as 
    possible to reduce space
    - For example, in the Knapsack Problem, we define our state by two parameter index and weight 
    ```
        DP[index][weight]
    ```
    - In the problem, index and weight combined together can uniquely identify a subproblem for the knapsack problem

+ Step 3: Formulating a relation among the states: 
    - This is the hardest part of DP because it requires a lot of intuition to find the pattern. Let's understand it with a sample problem: 

    ```
        Given 3 numbers {1, 3, 5}, we need to tell
        the total number of ways we can form a number 'N' 
        using the sum of the given three numbers.
        (allowing repetitions and different arrangements).

        Total number of ways to form 6 is: 8
        1+1+1+1+1+1
        1+1+1+3
        1+1+3+1
        1+3+1+1
        3+1+1+1
        3+3
        1+5
        5+1
    ```

    - Analysis: 
        + First, the parameter N will be the deciding state as it can uniquely identify any subproblem. In this problem, our state(n) is the total number of arrangements to form N using {1,3,5} as elements
        + As we can only use 1, 3 or 5 to form a give number. Let assume that we know the result for n = 1,2,3,4,5,6 or we can say, we know state(n = 1), state(n = 2), state(n=3),..., state(n = 6)

    - Code: 
    ```
        // Returns the number of arrangements to  
        // form 'n'  
        int solve(int n) 
        {  
        // base case 
        if (n < 1)  
            return 0; 
        if (n == 1)   
            return 1;   
        
        return solve(n-1) + solve(n-3) + solve(n-5); 
        }     

    ```

- However, the above code is still in exponential time as it is calculating the same state again and again. Therefore, we will need to add memoization to reduce the time complexity

+ Step 4: Adding memoization or tabulation to the state:
    - This is the eaisest part of Dynamic Programming solution. We just need to store the state answer so that the next time that state is required, we can directly use it from memory
    - We will go deeper into the concept of memoization below

    For now, here is how to work the above problem using memoization technique
    ```
        // initialize to -1 
        int dp[MAXN]; 
        
        // this function returns the number of  
        // arrangements to form 'n'  
        int solve(int n) 
        {  
        // base case 
        if (n < 1)   
            return 0; 
        if (n == 1)   
            return 1; 
        
        // checking if already calculated 
        if (dp[n]!=-1)  
            return dp[n]; 
        
        // storing the result and returning 
        return dp[n] = solve(n-1) + solve(n-3) + solve(n-5); 
        } 


    ```

    => Source code for this problem in Python: 


## Basic Concepts: 

- Recursion

- Tabulation: Bottom Up

    + Let’s describe a state for our DP problem to be dp[x] with dp[0] as base state and dp[n] as our destination state. So,  we need to find the value of destination state i.e dp[n].
    
   +  If we start our transition from our base state i.e dp[0] and follow our state transition relation to reach our destination state dp[n], we call it Bottom Up approach as it is quite clear that we started our transition from the bottom base state and reached the top most desired state.
   
- Memoization: Top Down

    + If we need to find the value for some state say dp[n] and instead of starting from the base state that i.e dp[0] we ask our answer from the states that can reach the destination state dp[n] following the state transition relation, then it is the top-down fashion of DP.
    
    + Here, we start our journey from the top most destination state and compute its answer by taking in count the values of states that can reach the destination state, till we reach the bottom most base state.


## Sample Problems: 

### Ugly Number: 

Problem Statement: 

```
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.


```

Dynamic Programming Approach: 

The ugly-number sequence is 1,2,3,4,5,6,8,10,12,15, ... because the number can only be divided by 2,3,5, one way to look at the sequence is to split the sequence to three group as below: 
(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …

Algorithm:

```
1. Declare an array for ugly numbers: ugly[n] with its size being equal to the nth element
2. Initialize the first ugly number: ugly[0] = 1
3. Initialize three array index variables i2, i3, i5 to point to the 1st element in the array: i2 = i3 = i5 = 0
4. Initialize 3 choices for the next ugly number: 
next_multiple_of_2 = ugly[i2] * 2
next_multiple_of_3 = ugly[i3] * 3
next_multiple_of_5 = ugly[i5] * 5

5. Now go in a loop to fill out all of the ugly numbers until 150
For(i = 1; i < 150; i++){
    next_ugly_no  = Min(next_mulitple_of_2,
                        next_mulitple_of_3,
                        next_mulitple_of_5); 

    ugly[i] =  next_ugly_no       

    if (next_ugly_no  == next_mulitple_of_2) 
    {             
        i2 = i2 + 1;        
        next_mulitple_of_2 = ugly[i2]*2;
    } 
    if (next_ugly_no  == next_mulitple_of_3) 
    {             
        i3 = i3 + 1;        
        next_mulitple_of_3 = ugly[i3]*3;
     }            
     if (next_ugly_no  == next_mulitple_of_5)
     {    
        i5 = i5 + 1;        
        next_mulitple_of_5 = ugly[i5]*5;
     } 
     
}/* end of for loop */ 

}
6.return next_ugly_nos
```

## Dynamic Programming Problem Pattern: 

- Minimum (Maximum) Path to reach a Target:
    
    + Statement: Given a target find minimum (maximum) cost / path / sum to reach the target.
    
    + Approach: Choose the minimum (maximum) path among all possible paths before the current state, then add the value for the current state.
    
            routes[i] = min(routes[i-1], routes[i-2], ... , routes[i-k]) + cost[i]
            
    + Optimal solutions for all values in the target and return all the value for the target

```
for (int i = 1; i <= target; ++i) {
   for (int j = 0; j < ways.size(); ++j) {
       if (ways[j] <= i) {
           dp[i] = min(dp[i], dp[i - ways[j]] + cost / path / sum) ;
       }
   }
}
 
return dp[target]

```
    
- Distinct Ways

- Merging Intervals: 

- DP on Strings

- Decision Making




