import unittest


from chess.board.square import Square
from chess.geometry.coordinate.coord import Coordinate


class SquareUnitTest(unittest.TestCase):

    def test_square_with_null_id_raises_error(self):
        with self.assertRaises(Exception):
            Square(square_id=None, name="name", coordinate=Coordinate(0,0))


    def test_square_with_negative_id_raises_error(self):
        with self.assertRaises(Exception):
            Square(square_id=-1, name="name", coordinate=Coordinate(0,0))


    def test_square_with_null_name_raises_error(self):
        with self.assertRaises(Exception):
            Square(square_id=1, name=None, coordinate=Coordinate(0,0))


    def test_square_with_blank_name_raises_error(self):
        with self.assertRaises(Exception):
            Square(square_id=-1, name=" ", coordinate=Coordinate(0,0))


    def test_square_with_name_below_min_length_raises_error(self):
        with self.assertRaises(Exception):
            Square(square_id=-1, name="a", coordinate=Coordinate(0,0))



if __name__ == '__main__':
    unittest.main()
