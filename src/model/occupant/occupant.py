from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from src.common.dimension import Dimension
from src.model.board.grid_coordinate import GridCoordinate



@dataclass
class Occupant:
    id: int
    dimension: Dimension
    coordinate: GridCoordinate = None
    cells: Optional[list[list['Cell']]] = None

    def occupy_cells(self, top_left_coord: GridCoordinate, cells: list[list['Cell']]):
        """
        Occupies the cells in the grid starting from the top-left coordinate.
        """
        self.coordinate = top_left_coord
        self.cells = cells
        for row in cells:
            for cell in row:
                cell.occupant = self

    def print_cells(self):
        """
        Prints the cells occupied by this occupant.
        """
        if self.cells is None:
            print("No cells occupied.")
            return

        mismatch_count = 0
        for row in self.cells:
            for cell in row:
                if cell.occupant != self:
                    print("Mismatch:" , mismatch_count, " for cell", cell.id, " at ", cell.coordinate)

                print(f"Cell {cell.id} at {cell.coordinate} is occupied by Occupant {self.id}.")
        print()




