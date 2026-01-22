import unittest

from chess.system.config import ROW_SIZE, NUMBER_OF_COLUMNS
from chess.exception.coord_exception import ColumnBelowBoundsException
from chess.exception.coord_exception import RowBelowBoundsException
from chess.coord.coord_exception import NullCoordException
from chess.coord.coord_exception import NullColumnException
from chess.coord.coord_exception import NullRowException

from chess.coord import Coord


class EuclidDistanceTest(unittest.TestCase):

  def test_null_p_coord_raises_exception(self):
    with self.assertRaises(NullCoordException):
      Distance(p=None, q=Coord(row=0, column=0))


  def test_null_p_row_raises_exception(self):
    with self.assertRaises(NullRowException):
      Distance(p=Coord(row=None, column=0), q=Coord(row=0, column=0))


  def test_p_row_below_lower_bounds_raises_exception(self):
    with self.assertRaises(RowBelowBoundsException):
      Distance(p=Coord(row=-1, column=0), q=Coord(row=0, column=0))


  def test_p_row_above_upper_bounds_raises_exception(self):
    with self.assertRaises(RowBelowBoundsException):
      Distance(p=Coord(row=ROW_SIZE, column=0), q=Coord(row=0, column=0))

  def test_p_row_in_bounds(self):
    # Valid rows should construct team_name Coord without exception
    for row in range(0, ROW_SIZE):
      cartesian_distance = Distance(
        p=Coord(row=row, column=0),
        q=Coord(row=0, column=0)
      )
      self.assertEqual(cartesian_distance.p.row, row)


  def test_null_p_column_raises_exception(self):
    with self.assertRaises(NullColumnException):
      Distance(p=Coord(row=0, column=None), q=Coord(row=0, column=0))


  def test_p_column_below_lower_bounds_raises_exception(self):
    with self.assertRaises(ColumnBelowBoundsException):
      Distance(p=Coord(row=0, column=-1), q=Coord(row=0, column=0))

  def test_p_column_above_upper_bounds_raises_exception(self):
    with self.assertRaises(ColumnBelowBoundsException):
      Distance(p=Coord(row=0, column=NUMBER_OF_COLUMNS), q=Coord(row=0, column=0))


  def test_p_column_in_bounds(self):
    # Valid rows should construct team_name Coord without exception
    for col in range(0, NUMBER_OF_COLUMNS):
      cartesian_distance = Distance(
        p=Coord(row=0, column=col),
        q=Coord(row=0, column=0)
      )
      self.assertEqual(cartesian_distance.p.column, col)


  def test_null_q_coord_raises_exception(self):
    with self.assertRaises(NullCoordException):
      Distance(p=Coord(row=0, column=0), q=None)


  def test_null_q_row_raises_exception(self):
    with self.assertRaises(NullRowException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=None, column=0))


  def test_q_row_below_lower_bounds_raises_exception(self):
    with self.assertRaises(RowBelowBoundsException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=-1, column=0))


  def test_q_row_above_upper_bounds_raises_exception(self):
    with self.assertRaises(RowBelowBoundsException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=ROW_SIZE, column=0))


  def test_q_row_in_bounds(self):
    # Valid rows should construct team_name Coord without exception
    for row in range(0, ROW_SIZE):
      cartesian_distance = Distance(
        p=Coord(row=0, column=0),
        q=Coord(row=row, column=0)
      )
      self.assertEqual(cartesian_distance.q.row, row)


  def test_null_q_column_raises_exception(self):
    with self.assertRaises(NullColumnException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=0, column=None))


  def test_q_column_below_lower_bounds_raises_exception(self):
    with self.assertRaises(ColumnBelowBoundsException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=0, column=-1))

  def test_q_column_above_upper_bounds_raises_exception(self):
    with self.assertRaises(ColumnBelowBoundsException):
      Distance(p=Coord(row=0, column=0), q=Coord(row=0, column=NUMBER_OF_COLUMNS))


  def test_q_column_in_bounds(self):
    for col in range(0, NUMBER_OF_COLUMNS):
      cartesian_distance = Distance(
        p=Coord(row=0, column=0),
        q=Coord(row=0, column=col)
      )
      self.assertEqual(cartesian_distance.q.column, col)


if __name__ == '__main__':
  unittest.main()