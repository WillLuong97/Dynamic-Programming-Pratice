import unittest
import DynamicProgramming
class Dynamic_Programming_Cases(unittest.TestCase):
#     def test_fibbonacci_RECURSION_1(self):
#         test_value = 1
#         desired_value = 1
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_2(self):
#         test_value = 2
#         desired_value = 1
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_3(self):
#         test_value = 3
#         desired_value = 2
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_4(self):
#         test_value = 4
#         desired_value = 3
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_5(self):
#         test_value = 5
#         desired_value = 5
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_6(self):
#         test_value = 6
#         desired_value = 8
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_7(self):
#         test_value = 7
#         desired_value = 13
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_8(self):
#         test_value = 8
#         desired_value = 21
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_10(self):
#         test_value = 10
#         desired_value = 55
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_12(self):
#         test_value = 12
#         desired_value = 144
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_RECURSION_35(self):
#         test_value = 35
#         desired_value = 9227465
#         result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
#         #assertion: 
#         self.assertEqual(result, desired_value)


#     def test_fibbonacci_MEMOIZATION_1(self):
#         test_value = 1
#         desired_val = 1
#         result = DynamicProgramming.fib_memo(test_value)
#         #Assertion: 
#         self.assertEqual(test_value, desired_val)

#     def test_fibbonacci_MEMOIZATION_35(self):
#         test_value = 35
#         desired_val = 9227465
#         result = DynamicProgramming.fib_memo(test_value)

#         #Assertion: 
#         self.assertEqual(result, desired_val)
        
#     def test_fibbonacci_MEMOIZATION_29(self):
#         test_value = 29
#         desired_val = 514229
#         result = DynamicProgramming.fib_memo(test_value)

#         #Assertion: 
#         self.assertEqual(result, desired_val)


#     def test_fibbonacci_BOTTOM_UP_1(self):
#         test_value = 1
#         desired_value = 1
#         result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
#         #assertion
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_BOTTOM_UP_35(self):
#         test_value = 35
#         desired_value = 9227465
#         result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
#         #assertion
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_BOTTOM_UP_43(self):
#         test_value = 43
#         desired_value = 433494437
#         result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
#         #assertion
#         self.assertEqual(result, desired_value)

#     def test_fibbonacci_BOTTOM_UP_100(self):
#         test_value = 100
#         desired_value = 354224848179261915075
#         result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
#         #assertion
#         self.assertEqual(result, desired_value)

# class Testing_For_Unique_Path_Algorithm(unittest.TestCase):
#     def test_unique_path_RECURSION_3_2(self):
#         test_row_value = 3
#         test_column_value = 2
#         desired_result = 3
#         result = DynamicProgramming.uniquePath_RECURSION(test_row_value, test_column_value)

#         #assertion checks: 
#         self.assertEqual(result, desired_result)

#     def test_unique_path_RECURSION_7_3(self):
#         test_column_value = 7
#         test_row_value = 3
#         desired_result = 28
#         result = DynamicProgramming.uniquePath_RECURSION(test_column_value, test_row_value)

#         #assertion check: 
#         self.assertEqual(desired_result, result)

#     def test_unique_path_Bottom_Up_3_2(self):
#         test_column_value = 3
#         test_row_value = 2  
#         desired_result = 3
#         result = DynamicProgramming.uniquePath_BottomUp(test_column_value, test_row_value)

#         #assertion check: 
#         self.assertEqual(desired_result, result)

#     def test_unique_path_Bottom_Up_7_3(self):
#         test_column_value = 7
#         test_row_value = 3
#         desired_result = 28

#         result = DynamicProgramming.uniquePath_BottomUp(test_column_value, test_row_value)

#         #assertion check: 
#         self.assertEqual(desired_result, result)


    def test_ugly_number_7_8(self):
        test_n = 7
        desired_result = 8
        calculated_result = DynamicProgramming.uglyNumber_TOPDOWN(test_n)

        #assertion test:
        self.assertEqual(desired_result, calculated_result)


    def test_ugly_number_10_12(self):
        test_n = 10
        desired_result = 12
        calculated_result = DynamicProgramming.uglyNumber_TOPDOWN(test_n)

        #assertion test:
        self.assertEqual(desired_result, calculated_result)


    def test_ugly_number_15_24(self):
        test_n = 15
        desired_result = 24
        calculated_result = DynamicProgramming.uglyNumber_TOPDOWN(test_n)

        #assertion test:
        self.assertEqual(desired_result, calculated_result)

    def test_ugly_number_150_5832(self):
        test_n = 150
        desired_result = 5832
        calculated_result = DynamicProgramming.uglyNumber_TOPDOWN(test_n)

        #assertion test:
        self.assertEqual(desired_result, calculated_result)

        


if __name__ == "__main__":
    unittest.main()