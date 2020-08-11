## Dynamic Programming

### Definition:

- In genearal, algorithm is an optimziation over plain recusion. The ided is to simply store the result of subproblems, so that we do not have to recompute them when needed later.

### Overalapping Subproblems

#### Optimal Substructure Property: 


#### How to solve a Dynamic Programming Problem: 
- Dynamic Programming (DP) aims to solve problem on polynomial time (n^k) from exponential time (2^n, etc.)

Steps to solve a DP: 
1. Check if it is a DP problem 
2. Decide a state expression with least parameters 
3. Formulate state relationship
4. Do tabulation (or add memoization)


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


### Basic Concepts: 

- Tabulation: Bottom Up
- Memoization: Top Down
