import unittest
from unittest.mock import Mock


from exception.exception import NullSquareEntryError, InvalidIdError, InvalidFigureHeightError, \
    OccupiedSquareEntryError, SelfOccupiedSquareError, InvalidFigureLengthError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError
from game.board.board_square import GameBoardSquare
from game.figure.game_figure import GameFigure


class TestGameFigure(unittest.TestCase):

    def setUp(self):
        self.mock_square = Mock()
        self.mock_square._occupant = None
        # Make `occupant` behave like a property that returns `_occupant`
        type(self.mock_square).occupant = property(lambda s: s._occupant)

        self.mock_figure = Mock(name="MockFigure")
        self.figure = GameFigure(_id=1, _length=2, _height=3)

    def test_constructing_figure_with_valid_id(self):
        """Test figure creation with valid ID"""
        figure = GameFigure(_id=1, _length=2, _height=3)
        self.assertEqual(figure.id, 1)

    def test_constructing_figure_with_invalid_id_raises_error(self):
        """Test figure creation with invalid ID"""
        with self.assertRaises(InvalidIdError):
            GameFigure(_id=-1, _length=2, _height=2)

    def test_constructing_figure_with_valid_length(self):
        figure = GameFigure(_id=1, _length=2, _height=3)
        self.assertGreaterEqual(figure._length, GameFigure.MINIMUM_LENGTH)

    def test_invalid_figure_length_throws_error(self):
        """Test figure creation with an invalid length"""
        with self.assertRaises(InvalidFigureLengthError):
            GameFigure(_id=1, _length=0, _height=2)

    def test_constructing_figure_with_valid_height(self):
        figure = GameFigure(_id=1, _length=2, _height=3)
        self.assertGreaterEqual(figure._height, GameFigure.MINIMUM_HEIGHT)

    def test_invalid_height_throws_error(self):
        """Test figure creation with invalid height"""
        with self.assertRaises(InvalidFigureHeightError):
            GameFigure(_id=1, _length=2, _height=0)

    def test_area_of_figure_greater_or_equal_minimum_area(self):
        """Test figure area is greater than or equal to the minimum area"""
        figure = GameFigure(_id=1, _length=2, _height=3)
        self.assertGreaterEqual(figure.area(), GameFigure.MINIMUM_AREA)

    def test_area_of_figure_below_minimum_raises_error(self):
        with self.assertRaises(FigureAreaBelowLimitError):
            GameFigure(_id=1, _length=GameFigure.MINIMUM_LENGTH, _height=GameFigure.MINIMUM_HEIGHT)

    def test_figure_entering_square_updates_square(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.figure.square, self.mock_square)

    def test_square_updates_occupant_on_figure_entered(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.mock_square.occupant, self.figure)

    def test_figure_entering_null_square_raises_error(self):
        with self.assertRaises(NullSquareEntryError):
            self.figure.enter_square(None)

    def test_figure_entering_square_it_already_occupies_raises_error(self):
        self.figure._square = self.mock_square
        self.mock_square._occupant = self.figure
        with self.assertRaises(SelfOccupiedSquareError):
            self.figure.enter_square(self.mock_square)

    def test_figure_entering_square_occupied_by_other_figure_raises_error(self):
        self.mock_figure._square = self.mock_square
        self.mock_square._occupant = self.mock_figure
        with self.assertRaises(OccupiedSquareEntryError):
            self.figure.enter_square(self.mock_square)

    def test_figure_leaving_square_sets_square_occupant_to_null(self):
        self.mock_square._occupant = self.figure
        self.figure._square = self.mock_square
        self.figure.leave_square()
        self.assertIsNone(self.mock_square.occupant)

    def test_figure_looses_ownership_of_square_on_exit(self):
        self.mock_square._occupant = self.figure
        self.figure._square = self.mock_square
        self.figure.leave_square()
        self.assertIsNone(self.figure.square)

    def test_figure_leaving_nonexistent_square_raises_error(self):
        self.figure._square = None
        with self.assertRaises(NoSquareToLeaveError):
            self.figure.leave_square()




if __name__ == '__main__':
    unittest.main()