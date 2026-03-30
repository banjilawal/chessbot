import unittest
from unittest.mock import patch

from chess.geometry.exception.coord import CoordValidationException
from unit.chess_test.geometry.coord_test import CoordTest


class PathTest(unittest):


  @patch('assurance.notification.point.CoordValidator.validate')
  def test_invalid_u_coord_raises_error(self, mock_coord_validation):
    mock_coord_validation.return_value.is_success.return_value = False
    mock_coord_validation.return_value.exception = CoordValidationException("Invalid ID")

    v = CoordTest.valid_mock_coord()


if __name__ == "__main__":
  unittest.main()