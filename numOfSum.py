#Python program to calculate the number of ways a number N can be formed based on a given set of number
#The program is an implemnetation of Dynamic Programming

#Function to calculate the number of ways three given number can add up to form a number N
#regular non-memoization method
def findNumOfSum_RECURSION(target):
    if target < 1:
        return 0

    if target == 1:
        return 1

    #recursive function to caculate through the state
    return findNumOfSum_RECURSION(target - 1) + findNumOfSum_RECURSION(target - 3) + findNumOfSum_RECURSION(target - 4)


#Adding memoization:
def findNumOfSum_RECURSION_Memo(target):
    #create an array to store already calculated values
    DP = [0 for i in range(0, target + 1)]

    #base case:
    DP[0] = DP[1] = DP[2] = 1
    DP[3] = 2

    #count ways for all values up to 'N' and store the result
    for i in range(4, target + 1):
        DP[i] = DP[i - 1] + DP[i - 3] + DP[i - 5]

    return DP[target]




    

#main function
def main():
    test_number = 6
    result = findNumOfSum_RECURSION_Memo(test_number)
    print(f"Number of ways from 1,3,5 to make ", test_number, " is: ", result)
main()

    