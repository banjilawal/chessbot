import unittest
from unittest.mock import Mock


from game.exception.exception import NullSquareEntryError, InvalidIdError, InvalidFigureHeightError, \
    OccupiedSquareEntryError, SelfOccupiedSquareError, InvalidFigureLengthError, NoSquareToLeaveError, \
    FigureAreaBelowLimitError
from game.model.occupant.obstacle import Obstacle


class TestGameFigure(unittest.TestCase):

    def setUp(self):
        self.mock_square = Mock()
        self.mock_square._occupant = None
        # Make `occupant` behave like a property that returns `_occupant`
        type(self.mock_square).occupant = property(lambda s: s._occupant)

        self.mock_figure = Mock(name="MockFigure")
        self.figure = Obstacle(id=1, length=2, height=3)

    def test_constructing_figure_with_valid_id(self):
        """Test occupant creation with valid ID"""
        figure = Obstacle(id=1, length=2, height=3)
        self.assertEqual(figure.id, 1)

    def test_constructing_figure_with_invalid_id_raises_error(self):
        """Test occupant creation with invalid ID"""
        with self.assertRaises(InvalidIdError):
            Obstacle(id=-1, length=2, height=2)

    def test_constructing_figure_with_valid_length(self):
        figure = Obstacle(id=1, length=2, height=3)
        self.assertGreaterEqual(figure.length, Obstacle.MINIMUM_LENGTH)

    def test_invalid_figure_length_throws_error(self):
        """Test occupant creation with an invalid length"""
        with self.assertRaises(InvalidFigureLengthError):
            Obstacle(id=1, length=0, height=2)

    def test_constructing_figure_with_valid_height(self):
        figure = Obstacle(id=1, length=2, height=3)
        self.assertGreaterEqual(figure.height, Obstacle.MINIMUM_HEIGHT)

    def test_invalid_height_throws_error(self):
        """Test occupant creation with invalid height"""
        with self.assertRaises(InvalidFigureHeightError):
            Obstacle(id=1, length=2, height=0)

    def test_area_of_figure_greater_or_equal_minimum_area(self):
        """Test occupant area is greater than or equal to the minimum area"""
        figure = Obstacle(id=1, length=2, height=3)
        self.assertGreaterEqual(figure.area(), Obstacle.MINIMUM_AREA)

    def test_area_of_figure_below_minimum_raises_error(self):
        with self.assertRaises(FigureAreaBelowLimitError):
            Obstacle(id=1, length=Obstacle.MINIMUM_LENGTH, height=Obstacle.MINIMUM_HEIGHT)

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
        self.figure.square = self.mock_square
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
        self.figure.square = self.mock_square
        self.figure.leave_square()
        self.assertIsNone(self.mock_square.occupant)

    def test_figure_looses_ownership_of_square_on_exit(self):
        self.mock_square._occupant = self.figure
        self.figure.square = self.mock_square
        self.figure.leave_square()
        self.assertIsNone(self.figure.square)

    def test_figure_leaving_nonexistent_square_raises_error(self):
        self.figure.square = None
        with self.assertRaises(NoSquareToLeaveError):
            self.figure.leave_square()




if __name__ == '__main__':
    unittest.main()