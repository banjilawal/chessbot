from itertools import count
from typing import List

from exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from game.board.board_square import GameBoardSquare

from dataclasses import dataclass
from typing import Optional

from game.figure.game_figure import GameFigure


@dataclass
class GameBoard:
    _id: int
    _number_of_rows: int
    _number_of_columns: int
    _figures: Optional[List[GameFigure]] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self.id < 0:
            raise InvalidIdError("figure id cannot be less than 1.")

        if self._number_of_rows < 2:
            raise InvalidNumberOfRowsError("Game board must have at least 2 number_of_rows.");
        if self._number_of_columns < 2:
            raise InvalidNumberOfColumnsError("Game board must have at least 2 number_of_columns.");

        index = count(1)
        self._squares = [
            [
                GameBoardSquare(id=next(index), row=row, column=column)
                for column in range(self._number_of_columns)
            ]
            for row in range(self._number_of_rows)
        ]

    @property
    def number_of_rows(self):
        return self._number_of_rows

    @property
    def number_of_columns(self):
        return self.number_of__columns

    @property
    def squares(self):
        return self._squares

    @property
    def figures(self):
        return self._figures

    def area(self):
        return self._number_of_rows * self._number_of_columns

