import unittest
from unittest.mock import patch

from assurance.exception.validation.coord import CoordinateValidationException
from unit.chess_test.geometry.coord.coord_test import CoordinateTest


class PathTest(unittest):


    @patch('assurance.validators.coord.CoordinateValidator.validate')
    def test_invalid_u_coord_raises_error(self, mock_coord_validation):
        mock_coord_validation.return_value.is_success.return_value = False
        mock_coord_validation.return_value.exception = CoordinateValidationException("Invalid ID")

        v = CoordinateTest.valid_mock_coordinate()


if __name__ == "__main__":
    unittest.main()