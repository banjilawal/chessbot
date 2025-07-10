from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.grid_entity import GridEntity


@dataclass
class VerticalMover(GridEntity):
    def __init__(self, mover_id: int, length: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=mover_id, dimension=Dimension(length=length, height=1), coordinate=coordinate)


@dataclass
class HorizontalMover(GridEntity):
    def __init__(self, mover_id: int, height: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=mover_id, dimension=Dimension(length=1, height=height), coordinate=coordinate)




