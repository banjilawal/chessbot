from dataclasses import dataclass
from typing import Optional

from src.common.dimension import Dimension
from model.grid_coordinate import GridCoordinate



@dataclass
class GridEntity:
    id: int
    dimension: Dimension
    coordinate: GridCoordinate = None
    cells: Optional[list[list['Cell']]] = None



