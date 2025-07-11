from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING

from model.cell import Cell
from src.common.dimension import Dimension
from model.grid_coordinate import GridCoordinate

if TYPE_CHECKING:
    from model.cell import Cell

@dataclass
class GridEntity:
    dimension: Dimension
    top_left_coordinate: Optional[GridCoordinate] = None

@dataclass
class BrikPallet(GridEntity):
    pass

@dataclass(kw_only=True)
class Mover(GridEntity, ABC):
    id: int

    @abstractmethod
    def move(self, board: 'Board', destination_coordinate: GridCoordinate) -> None:
        pass


git commit -m "Changed GridEmtity hiereach to Mover<--GricEntity-->BrickPallet. model.Mover has: 1) id field. 2) move(self, BOARD, GridCoordinate)"
