from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from common.game_color import GameColor
from model.board.grid_coordinate import GridCoordinate

from common.dimension import Dimension

if TYPE_CHECKING:
    from model.cell.cell import Cell


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




