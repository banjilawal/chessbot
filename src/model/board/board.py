from itertools import count
from typing import List


from src.common.game_constant import GameConstant
from src.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from src.model.cell.cell import Cell

from dataclasses import dataclass
from typing import Optional

from src.model.occupant.obstacle import Obstacle

@dataclass
class Board:
    MINIMUM_NUMBER_OF_ROWS = 2
    MINIMUM_NUMBER_OF_COLUMNS = 2
    id: int
    num_rows: int
    num_columns: int
    figures: Optional[List[Obstacle]] = None

    # Drawing constants as class attributes
    SQUARE_SIZE_IN_PIXELS = 40

    # Pygame colors (defined as RGB tuples)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY_LIGHT = (200, 200, 200)
    GRAY_DARK = (150, 150, 150)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    def __post_init__(self):
        if self.id < GameConstant.MINIMUM_ID:
            raise InvalidIdError("GameBoard id below minimum value.")
        if self.num_rows < Board.MINIMUM_NUMBER_OF_ROWS:
            raise InvalidNumberOfRowsError("GameBoard num_rows below minimum value.")
        if self.num_columns < Board.MINIMUM_NUMBER_OF_COLUMNS:
            raise InvalidNumberOfColumnsError("GameBoard num_columns below minimum value.")

        index = count(1)
        self._squares = [
            [
                Cell(_id=next(index), _row=row, _column=column)
                for column in range(self.num_columns)
            ]
            for row in range(self.num_rows)
        ]

    @property
    def columns(self):
        return self.num_columns

    @property
    def squares(self):
        return self._squares

    def area(self):
        return self.num_rows * self.num_columns



    def print_grid(self): # Keeping your original method for text-based printing
        for row in self._squares:
            print("".join("+---" for _ in row) + "+")
            print("".join("|   " for _ in row) + "|")
        print("".join("+---" for _ in self._squares[0]) + "+")