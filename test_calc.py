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

if __name__ == '__main__':
    unittest.main()
