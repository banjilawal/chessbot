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
    cells: tuple[tuple['Cell', ...], ...] = field(init=False, repr=False)

    def __post_init__(self):
        cell_grid = tuple(
            tuple(Cell() for w in range(self.dimension.length))
            for h in range(self.dimension.height)
        )
        object.__setattr__(self, 'cells', cell_grid)
