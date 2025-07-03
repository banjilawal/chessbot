from dataclasses import dataclass, field
from typing import Optional, Tuple, List

from exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError
from model.board.grid_coordinate import GridCoordinate
from model.occupant.crate import Crate
from common.dimension import Dimension
from model.portal.door import Door
from model.occupant.boulder import Boulder
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError
from src.model.cell.cell import Cell


@dataclass(frozen=True)
class Board:
    MIN_ROW_COUNT = 2
    MIN_COLUMN_COUNT = 2

    id: int
    portal: Optional[Door] = None
    crates: Tuple[Crate, ...] = field(default_factory=tuple)
    boulders: List[Boulder] = field(default_factory=list)
    cells: Tuple[Tuple[Cell, ...], ...] = field(init=False, repr=False)

    dimension: Dimension = field(default_factory=lambda: Dimension(length=GameDefault.COLUMN_COUNT, height=GameDefault.ROW_COUNT))

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Board id below minimum value.")

        if self.dimension.height < self.MIN_ROW_COUNT:
            raise InvalidNumberOfRowsError("Board number of rows below minimum value.")

        if self.dimension.length < self.MIN_COLUMN_COUNT:
            raise InvalidNumberOfColumnsError("Board number of columns below minimum value.")

        # Create the grid of cells with correct coordinates
        rows_list = [] # Use a list for building, then convert to tuple
        for row_index in range(self.dimension.height):
            current_row_list = []
            for column_index in range(self.dimension.length):
                # Correctly assign the cell's own row and column to its coordinate
                cell_id = row_index * self.dimension.length + column_index + 1 # More standard ID calculation
                cell = Cell(id=cell_id, coordinate=GridCoordinate(row=row_index, column=column_index))
                current_row_list.append(cell)
            rows_list.append(tuple(current_row_list)) # Convert inner list to tuple

        # Set the cells attribute using object.__setattr__ for frozen dataclass
        object.__setattr__(self, 'cells', tuple(rows_list)) # Convert outer list to tuple


    def row_count(self) -> int:
        return self.dimension.height

    def column_count(self) -> int:
        return self.dimension.length

    def add_boulder(self, boulder: Boulder):
        self.boulders.append(boulder)

    def add_boulders(self, boulders: List[Boulder]):
        self.boulders.extend(boulders)

    def are_occupied(self, top_left_coord: GridCoordinate, dimension: Dimension) -> bool:
        """
        Check if the cells starting from the top-left coordinate with the given dimension are occupied.
        """
        for row in range(top_left_coord.row, top_left_coord.row + dimension.height):
            for col in range(top_left_coord.column, top_left_coord.column + dimension.length):
                if self.cells[row][col].occupant is not None:
                    return True
        return False

    def print(self):
        """Print the board with cell IDs"""
        for row in self.cells:
            # Top border of the row
            print("".join("+---" for _ in row) + "+")
            # Cell IDs in the row, centered in each cell
            print("".join(f"|{cell.id:^3}" for cell in row) + "|")
        # Bottom border of the final row
        print("".join("+---" for _ in self.cells[0]) + "+")