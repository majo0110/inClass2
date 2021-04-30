import unittest
import calculator

class testCase_Add(unittest.TestCase):
    def test_add(self):
        result = calculator.addition(10,10)
        self.assertEqual(result, 20)

    def test_add_neg(self):
        self.assertEqual(calculator.addition(15,-30), -15)

    def test_add_string(self):
        self.assertRaises(TypeError, calculator.addition('hello', 'world'))

class testCase_Sub(unittest.TestCase):
    def test_sub(self):
        result = calculator.subtraction(10,15)
        self.assertEqual(result, -5)

    def test_sub_neg(self):
        self.assertEqual(calculator.subtraction(15,-30), 45)

    def test_sub_zero(self):
        self.assertEqual(calculator.subtraction(1000,0), 1000)

class testCase_mult(unittest.TestCase):
    def test_mult(self):
        result = calculator.multiplication(100,15)
        self.assertEqual(result, 1500)

    def test_mult_neg(self):
        self.assertEqual(calculator.multiplication(45,-30), -1350)

    def test_mult_zero(self):
        self.assertEqual(calculator.multiplication(15000,0), 0)

class testCase_division(unittest.TestCase):
    def test_division(self):
        result = calculator.division(30,15)
        self.assertEqual(result, 2)

    def test_division_neg(self):
        self.assertEqual( calculator.division(100, -40), -2.5)

    def test_division_zeor(self):
        self.assertRaises(ZeroDivisionError, calculator.division, 30,0)


if __name__ == '__main__':
    unittest.main()
