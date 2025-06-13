from itertools import count
from typing import List

from game.common.game_constant import GameConstant
from game.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from game.board.board_square import GameBoardSquare

from dataclasses import dataclass
from typing import Optional

from game.figure.game_figure import GameFigure


@dataclass
class GameBoard:
    MINIMUM_NUMBER_OF_ROWS = 2
    MINIMUM_NUMBER_OF_COLUMNS = 2
    _id: int
    _number_of_rows: int
    _number_of_columns: int
    _figures: Optional[List[GameFigure]] = None

    def __post_init__(self):
        """Validate initialization parameters"""
        if self._id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("GameBoard id below minimum value.")

        if self._number_of_rows < GameBoard.MINIMUM_NUMBER_OF_ROWS:
            raise InvalidNumberOfRowsError("GameBoard number_of_rows below minimum value.");
        if self._number_of_columns < GameBoard.MINIMUM_NUMBER_OF_COLUMNS:
            raise InvalidNumberOfColumnsError("GameBoard number_of_columns below minimum value.");

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
        return self.number_of_columns

    @property
    def squares(self):
        return self._squares

    @property
    def figures(self):
        return self._figures

    def area(self):
        return self._number_of_rows * self._number_of_columns

