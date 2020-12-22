#1314. Matrix Block Sum
'''
Problem statement: 
Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

'''
def matrixBlockSum(mat, K):
    #base case: 
    if len(mat) == 0:
        return [[]]

    #create an answer grid
    answer = [[0] * len(mat[0]) for _ in range(len(mat))]
    #helper method to find the sum of the block
    def add(mat, lowerR, upperR, lowerC, UpperC):
        #base case: 
        m = len(mat)
        n = len(mat[0])
        #check for valid grid position: 
        if lowerR < 0:
            lowerR = 0
        
        if upperR > m - 1:
            upperR = m-1

        if lowerC < 0:
            lowerC = 0

        if UpperC > n-1:
            UpperC = n-1


        blockSum = 0
        for r in range(lowerR, upperR+1):
            for c in range(lowerC, UpperC+1):
                blockSum += mat[r][c]
        return blockSum

    #loop through the original grid to find i and j
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            #identify the condition for r and c and calculate the sum 
            answer[i][j] = add(mat, i-K, i+K, j-K, j+K)
    return answer


        # m = len(mat)
        # n = len(mat[0])
        
		# # initialize the output
        # answer = [[0 for j in range(n)] for i in range(m)]
        
		# # code up the instructions with the max/min trick
        # for i in range(m):
        #     for j in range(n):
        #         answer[i][j] = sum(
        #             mat[r][c] for r in range(max(0, i-K), min(m, i+K+1)) 
        #                       for c in range(max(0, j - K), min(n, j+K+1))
        #         )
        
        # return answer



#main function to run the test cases
def main():
    print("TESTING MATRIX BLOCK SUM...")
    mat_1 = [[1,2,3],[4,5,6],[7,8,9]]
    k_1 = 1

    mat_2 = [[1,2,3],[4,5,6],[7,8,9]]
    K_2 = 2

    print(matrixBlockSum(mat_1, k_1))
    print(matrixBlockSum(mat_2, K_2))
    
    print("END OF TESTING...")
main()