import unittest
from unittest.mock import Mock

from game.piece.game_figure import GameFigure


class TestGameFigure(unittest.TestCase):

    def setUp(self):
        self.mock_square = Mock()
        self.mock_square._occupant = None
        # Make `occupant` behave like a property that returns `_occupant`
        type(self.mock_square).occupant = property(lambda s: s._occupant)

        self.mock_figure = Mock(name="MockFigure")  # You can reuse this

        self.figure = GameFigure(id=1, width=2, length=3)

    def test_enter_square_updates_square(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.figure.square, self.mock_square)

    def test_enter_square_updates_occupant(self):
        self.figure.enter_square(self.mock_square)
        self.assertIs(self.mock_square.occupant, self.figure)

    def test_enter_square_occupied_by_self_raises_error(self):
        self.figure._square = self.mock_square
        with self.assertRaises(ValueError):
            self.figure.enter_square(Mock())

    def test_enter_square_already_occupied_raises_error(self):
        self.mock_square.occupied = True
        with self.assertRaises(ValueError):
            self.figure.enter_square(self.mock_square)

if __name__ == '__main__':
    unittest.main()
