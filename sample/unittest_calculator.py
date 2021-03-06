import unittest
import calculator


class CalculatorTestCases(unittest.TestCase):

    def setUp(self):
        self.sut = calculator.Calculator

    def test_add(self):
        operand1, operand2 = 4, 5
        self.assertEqual(self.sut.add(operand1, operand2), 9, "Incorrect Calculator.add.")

    def test_sub(self):
        operand1, operand2 = 4, 5
        self.assertEqual(self.sut.subtract(operand1, operand2), -1, "Incorrect Calculator.subtract.")

    def test_mult(self):
        operand1, operand2 = 4, 5
        self.assertEqual(self.sut.multiply(operand1, operand2), 20, "Incorrect Calculator.multiply.")

    def test_div(self):
        operand1, operand2 = 4, 5
        self.assertEqual(self.sut.divide(operand1, operand2), 0, "Incorrect Calculator.divide.")

    def test_negate(self):
        operand = -10
        self.assertEqual(self.sut.negate(operand), -operand, "Incorrect Calculator.negate.")
        operand = 9
        self.assertEqual(self.sut.negate(operand), -operand, "Incorrect Calculator.negate.")

    def test_floorDiv(self):
        operand1, operand2 = 5, 2
        self.assertEqual(self.sut.floorDiv(operand1, operand2), 2, "Incorrect Calculator.floorDiv")

    def test_floorDivAssign(self):
        operand1, operand2 = 5, 2
        self.assertEqual(self.sut.floorDivAssign(operand1, operand2), 2, "Incorrect Calculator.floorDivAssign")

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()