import unittest
import DynamicProgramming
class Dynamic_Programming_Cases(unittest.TestCase):
    def test_fibbonacci_RECURSION_1(self):
        test_value = 1
        desired_value = 1
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_2(self):
        test_value = 2
        desired_value = 1
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_3(self):
        test_value = 3
        desired_value = 2
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_4(self):
        test_value = 4
        desired_value = 3
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_5(self):
        test_value = 5
        desired_value = 5
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_6(self):
        test_value = 6
        desired_value = 8
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_7(self):
        test_value = 7
        desired_value = 13
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_8(self):
        test_value = 8
        desired_value = 21
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_10(self):
        test_value = 10
        desired_value = 55
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_12(self):
        test_value = 12
        desired_value = 144
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)

    def test_fibbonacci_RECURSION_35(self):
        test_value = 35
        desired_value = 9227465
        result = DynamicProgramming.find_fibonacci_RECURSION(test_value)
        #assertion: 
        self.assertEqual(result, desired_value)


    def test_fibbonacci_MEMOIZATION_1(self):
        test_value = 1
        desired_val = 1
        result = DynamicProgramming.fib_memo(test_value)
        #Assertion: 
        self.assertEqual(test_value, desired_val)

    def test_fibbonacci_MEMOIZATION_35(self):
        test_value = 35
        desired_val = 9227465
        result = DynamicProgramming.fib_memo(test_value)

        #Assertion: 
        self.assertEqual(result, desired_val)
        
    def test_fibbonacci_MEMOIZATION_29(self):
        test_value = 29
        desired_val = 514229
        result = DynamicProgramming.fib_memo(test_value)

        #Assertion: 
        self.assertEqual(result, desired_val)


    def test_fibbonacci_BOTTOM_UP_1(self):
        test_value = 1
        desired_value = 1
        result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
        #assertion
        self.assertEqual(result, desired_value)

    def test_fibbonacci_BOTTOM_UP_35(self):
        test_value = 35
        desired_value = 9227465
        result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
        #assertion
        self.assertEqual(result, desired_value)

    def test_fibbonacci_BOTTOM_UP_43(self):
        test_value = 43
        desired_value = 433494437
        result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
        #assertion
        self.assertEqual(result, desired_value)

    def test_fibbonacci_BOTTOM_UP_100(self):
        test_value = 100
        desired_value = 354224848179261915075
        result = DynamicProgramming.find_fibonacci_BOTTOM_UP(test_value)
        #assertion
        self.assertEqual(result, desired_value)



if __name__ == "__main__":
    unittest.main()