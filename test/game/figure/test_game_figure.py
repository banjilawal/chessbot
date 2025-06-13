import unittest
from unittest.mock import Mock

from game.piece.game_figure import GameFigure


class TestGameFigure(unittest.TestCase):

    def setUp(self):
        self.mock_square = Mock()
        self.mock_square._occupant = None
        # Make `occupant` behave like a property that returns `_occupant`
        type(self.mock_square).occupant = property(lambda s: s._occupant)

        self.mock_figure = Mock(name="MockFigure")
        self.figure = GameFigure(_id=1, width=2, length=3)

    def test_enter_square_updates_square(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.figure.square, self.mock_square)

    def test_enter_square_updates_occupant(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.mock_square.occupant, self.figure)

    def test_enter_null_square_raises_error(self):
        with self.assertRaises(ValueError):
            self.figure.enter_square(None)

    def test_enter_square_occupied_by_self_raises_error(self):
        self.figure._square = self.mock_square
        with self.assertRaises(ValueError):
            self.figure.enter_square(Mock())

    def test_enter_square_already_occupied_raises_error(self):
        self.mock_figure._square = self.mock_square
        self.mock_square._occupant = self.mock_figure
        with self.assertRaises(ValueError):
            self.figure.enter_square(self.mock_square)

    def test_leave_square_sets_square_occupant_null(self):
        self.mock_square._occupant = self.figure
        self.figure._square = self.mock_square

    def test_leave_square_sets_square_owned_by_figure_null(self):
        self.mock_square._occupant = self.figure
        self.figure._square = self.mock_square

        self.figure.leave_square()
        self.assertIsNone(self.figure.square)

    def test_leave_square_which_is_null_throws_error(self):
        self.figure._square = None
        with self.assertRaises(ValueError):
            self.figure.leave_square()

if __name__ == '__main__':
    unittest.main()
