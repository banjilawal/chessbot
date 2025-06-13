from dataclasses import dataclass
from typing import Optional


@dataclass
class GameBoardSquare:
    id: int
    row: int
    column: int
    _occupant: Optional['GameFigure'] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 0:
            raise ValueError("grid cell id cannot be negative.")
        if self.row < 0:
            raise ValueError("grid coordinate row cannot be negative.")
        if self.column < 0:
            raise ValueError("grid coordinate column cannot be negative.")

    @property
    def occupant(self) -> Optional['GameFigure']:
        return self._occupant

    @property
    def occupied(self) -> bool:
        return self._occupant is not None

    def __repr__(self) -> str:
        status = f"Occupied by {self._occupant}" if self.occupied else "Empty"
        return f"Square({self.row}, {self.column}) - {status}"

# from game.figure.game_figure import GameFigure
#
# class GameBoardSquare:
#     def __init__(self, id: int, row: int, column: int):
#         """
#         Initialize a square on the game board.
#
#         :param row: The board_row position of the square on the board.
#         :param column: The column position of the square on the board.
#         """
#         if id < 0:
#             raise ValueError("grid cell id cannot be negative.")
#         if row < 0:
#             raise ValueError("grid coordinate row cannot be negative.")
#         if column < 0:
#             raise ValueError("grid coordinate column cannot be negative.")
#
#         self._id = id
#         self._row = row
#         self._column = column
#         self._occupant: GameFigure = None
#
#     @property
#     def id(self):
#         return self._id
#
#     @property
#     def row(self):
#         return self._row
#
#     @property
#     def column(self):
#         return self._column
#
#     @property
#     def color(self):
#         return self.color
#
#     @property
#     def occupant(self):
#         return self.occupant
#
#     @occupant.setter
#     def occupant(self, occupant: GameFigure):
#         self._occupant = occupant
#
#     @property
#     def occupied(self):
#         return self.occupant is not None
#
#     def __eq__(self, other):
#         if other is self:
#             return True
#         if other is None:
#             return False
#         if isinstance(other, GameBoardSquare):
#             return self._id == other.id and self._row == other.row and self._column == other.column
#         else :
#             return False
#
#     def __hash__(self):
#         return hash((self._id, self._row, self._column))
#
#     def occupy(self, game_figure: GameFigure):
#         """
#         Marks the square as occupied by a figure or player.
#
#         :param game_figure: The object or identifier representing the occupant.
#         """
#         if game_figure is None:
#             raise ValueError("a null game figure cannot occupy a square.")
#
#         if self.occupant is not None:
#             raise ValueError("square already occupied.")
#
#         if self._occupant.__eq__(game_figure):
#             return
#
#         self.occupant = game_figure
#
#     def vacate(self):
#         """
#         Marks the square as unoccupied.
#         """
#         self.occupied = False
#         self.occupant = None
#
#     def is_occupied(self):
#         if self.occupant is None:
#             return False
#         else:
#             return True
#         """
#         Checks whether the square is currently occupied.
#
#         :return: True if occupied, False otherwise.
#         """
#         return self.occupied
#
#     def __repr__(self):
#         """
#         String representation of the grid square.
#         """
#         status = f"Occupied by {self.occupant}" if self.occupied else "Empty"
#         return f"Square({self.row}, {self.col}) - {status}"
