from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from src.common.dimension import Dimension
from src.model.board.grid_coordinate import GridCoordinate



@dataclass
class GridEntity:
    id: int
    dimension: Dimension
    coordinate: GridCoordinate = None
    cells: Optional[list[list['Cell']]] = None



