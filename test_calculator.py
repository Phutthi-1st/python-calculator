import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    #Add test case
    def test_add_1(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_2(self):
        self.assertEqual(self.calc.add(100, -54), 46)

    #Sub test case
    def test_sub_1(self):
        self.assertEqual(self.calc.subtract(10, 2), 8)
        
    def test_sub_neg(self):
        self.assertEqual(self.calc.subtract(10, -50), 60)

    #Multi Test case
    def test_mul_1(self):
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_mul_2(self):
        self.assertEqual(self.calc.multiply(-3, 5), -15)

    #Divide Test case
    def test_div_1(self):
        self.assertEqual(self.calc.divide(10, 10), 1)
    
    def test_div_2(self):
        self.assertEqual(self.calc.divide(500, 10), 50)

    #Modulo Test case
    def test_mod_1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_mod_2(self):
        self.assertEqual(self.calc.modulo(144, 12), 0)

if __name__ == '__main__':
    unittest.main()