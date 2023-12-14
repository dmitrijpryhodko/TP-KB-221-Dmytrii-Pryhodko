from lab_04 import *
import unittest

class TestCalculator(unittest.TestCase):

    def test_isNumber(self):
        self.assertTrue(isNumber('123'))
        self.assertFalse(isNumber('+'))
        self.assertFalse(isNumber('*'))

    def test_math_operation(self):
        self.assertEqual(math_operation('+'), 0)
        self.assertEqual(math_operation('*'), 1)
        self.assertEqual(math_operation('^'), 2)

    def test_Rpn(self):
        self.assertEqual(Rpn('50 / 10 + 20 * 2 * ( 24 / 2 ) ^ 2'), ['50', '10', '/', '20', '2', '*', '24', '2', '/', '2', '^', '*', '+'])
        self.assertEqual(Rpn('120 / 3 + 112 * 20 * ( 45 / 5 ) ^ 2'), ['120', '3', '/', '112', '20', '*', '45', '5', '/', '2', '^', '*', '+'])

    def test_RpnRes(self):
        self.assertEqual(RpnRes(['50', '10', '/', '20', '2', '*', '24', '2', '/', '2', '^', '*', '+']), [5765.0])
        self.assertEqual(RpnRes(['120', '3', '/', '112', '20', '*', '45', '5', '/', '2', '^', '*', '+']), [181480.0])

if __name__ == '__main__':
    unittest.main()
    