from itertools import count
from typing import List

from game.board.board_square import GameBoardSquare
from game.piece.game_figure import GameFigure


class GameBoard:
    DEFAULT_DIMENSION = 4
    def __init__(self, rows: int, columns):
        if rows  < 2:
            raise ValueError("Game board must have at least 2 rows.");
        if columns < 2:
            raise ValueError("Game board must have at least 2 columns.");

        self._rows = rows
        self._columns = columns
        self._figures: List[GameFigure] = []
        self._squares: List[List[GameBoardSquare]] = []

        index = count(1)
        self._grid = [
            [
                GameBoardSquare(id=next(index), row=row, column=column)
                for column in range(self.columns)
            ]
            for row in range(self.rows)
        ]

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def squares(self):
        return self._squares

    @property
    def figures(self):
        return self._figures

    def area(self):
        return self.rows * self.columns

    """
    Private method to create a grid cell at the specified coordinate.
    """
    # def _create_cell(self, id: int, row: int, column: int):
    #     return GameBoardSquare(id=id, row=row, column=column)

