from itertools import count
from typing import List


from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError, InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from src.model.cell.cell import Cell

from dataclasses import dataclass, field
from typing import Optional

from src.model.occupant.obstacle import Obstacle

# The Board class represents a game board with a grid of cells. The board is initialized with a specific number of
# rows and columns, and it can contain obstacles. Each cell in the board is represented by an instance
# of the Cell class.
# The board cannot be changed during play. It's number of rows, columns and the 2D array of cells are immutable.
@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2
    id: int
    row_count: int
    column_count: int
    figures: Optional[List[Obstacle]] = None

    # 2D list of immutable cells that is filled after Board initialization.
    cells: tuple[tuple[Cell, ...], ...] = field(init=False)

    def __init__(self, id: int, row_count: int = GameDefault.COLUMN_COUNT, column_count: int = GameDefault.ROW_COUNT):
        if id < GameDefault.MIN_ID:
            raise InvalidIdError("Board id below minimum value.")
        if row_count < Board.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError("Board num_rows below minimum value.")
        if column_count < Board.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError("Board num_columns below minimum value.")

        # Using object.__setattr__ to bypass the frozen dataclass restriction for setting attributes.
        # Need to use object.__setattr__ for frozen classes. You cannot use self.attribute = value with frozen dataclasses.
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'row_count', row_count)
        object.__setattr__(self, 'column_count', column_count)
    #

    def __post_init__(self):
        rows = []
        for row in range(self.row_count):
            current_row = []
            for column in range(self.column_count):
                cell_id = row * self.column_count + column + 1
                cell = Cell(id=cell_id, row=row, column=column)
                current_row.append(cell)
            rows.append(tuple(current_row))

        # If sycnronization issues cause attribute setting of cells to freeze. This can happen when there is complex
        # setups in __post_init__, using object.__setattr__ to bypass the dataclass field initialization so we don't
        # run into issues with frozen dataclass fields. that can raise errors like "cannot assign to field 'cells'".
        object.__setattr__(self, 'cells', tuple(rows))

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