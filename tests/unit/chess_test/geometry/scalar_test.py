import unittest

from assurance.exception.validation.scalar import ScalarValidationException
from chess.common.config import BOARD_DIMENSION
from chess.exception.null.number import NullNumberException


from chess.exception.null.scalar import NullScalarException
from chess.exception.vector.scalar import ScalarBelowLowerBoundException, ScalarAboveUpperBoundException
from chess.geometry.scalar import Scalar


class ScalarTest(unittest.TestCase):

    def test_null_value_raises_exception(self):

        with self.assertRaises(NullNumberException):
            Scalar(value=None)

    def test_value_less_than_lower_bound_raises_exception(self):
        with self.assertRaises(ScalarBelowLowerBoundException):
            Scalar(value=-BOARD_DIMENSION)


    def test_value_greater_or_equal_board_dimension_raises_exception(self):
        with self.assertRaises(ScalarAboveUpperBoundException):
            Scalar(value=BOARD_DIMENSION)

    def test_valid_value_sets_correctly(self):
        for valid_value in range(1, BOARD_DIMENSION):
            scalar = Scalar(value=valid_value)
            # print(f"\nTesting scalar value: {scalar.value} expected={valid_value}")
            self.assertEqual(scalar.value, valid_value)


if __name__ == '__main__':
    unittest.main()
