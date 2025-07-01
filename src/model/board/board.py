from itertools import count
from typing import List


from src.common.game_constant import GameConstant
from src.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from src.model.cell.cell import Cell

from dataclasses import dataclass, field
from typing import Optional

from src.model.occupant.obstacle import Obstacle

@dataclass
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2
    id: int
    row_count: int
    column_count: int
    figures: Optional[List[Obstacle]] = None

    # 2D list of immutable cells that is filled after Board initialization.
    cells: tuple[tuple[Cell, ...], ...] = field(init=False)

    def __init__(self, id: int, row_count: int, column_count: int):
        if id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("Board id below minimum value.")
        if row_count < Board.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError("Board num_rows below minimum value.")
        if column_count < Board.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError("Board num_columns below minimum value.")

        self.id = id
        self.row_count = row_count
        self.column_count = column_count
    #


    def __post_init__(self):

        index = count(1)
        self._squares = [
            [
                Cell(_id=next(index), _row=row, _column=column)
                for column in range(self.column_count)
            ]
            for row in range(self.row_count)
        ]

    @property
    def columns(self):
        return self.column_count

    @property
    def squares(self):
        return self._squares

    def area(self):
        return self.row_count * self.column_count



    def print_grid(self): # Keeping your original method for text-based printing
        for row in self._squares:
            print("".join("+---" for _ in row) + "+")
            print("".join("|   " for _ in row) + "|")
        print("".join("+---" for _ in self._squares[0]) + "+")