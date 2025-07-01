from typing import List

from model.board.grid_coordinate import GridCoordinate
from model.occupant.escape_portal import EscapePortal
from model.occupant.boulder import Boulder
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

    portal: EscapePortal
    walls: Optional[List[Boulder]] = None
    obstacles: Optional[List[Obstacle]] = None
    # 2D list of immutable cells that is filled after Board initialization.
    cells: tuple[tuple[Cell, ...], ...] = field(init=False, repr=False)

    row_count: int = field(default=GameDefault.ROW_COUNT)
    column_count: int = field(default=GameDefault.COLUMN_COUNT)



    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Board id below minimum value.")
        if self.row_count < Board.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError("Board num_rows below minimum value.")
        if self.column_count < Board.MIN_COLUMN_COUNT:
             raise InvalidNumberOfRowsError("Board num_rows below minimum value.")
        if self.column_count < Board.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError("Board num_columns below minimum value.")
        rows = []
        for row in range(self.row_count):
            current_row = []
            for column in range(self.column_count):
                cell_id = row * self.column_count + column + 1
                cell = Cell(id=cell_id, coordinate=GridCoordinate(row=row, column=column))
                current_row.append(cell)
            rows.append(tuple(current_row))
        object.__setattr__(self, 'cells', tuple(rows))


    def area(self):
        return self.row_count * self.column_count

    def print(self):
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")

            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")

        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")
