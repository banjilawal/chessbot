from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict, TYPE_CHECKING

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.grid_entity import GridEntity
from strategy.horizontal_movement_strategy import HorizontalMovementStrategy

if TYPE_CHECKING:
    from model.grid import Grid


@dataclass
class VerticalMover(GridEntity):
    def __init__(self, mover_id: int, length: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=mover_id, dimension=Dimension(length=length, height=1), coordinate=coordinate)


@dataclass
class HorizontalMover(GridEntity):
    movement_strategy: HorizontalMovementStrategy = field(default_factory=HorizontalMovementStrategy)
    def __init__(self, mover_id: int, height: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=mover_id, dimension=Dimension(length=1, height=height), coordinate=coordinate)
        self.movement_strategy = HorizontalMovementStrategy()

    def move(self, grid: 'Grid', direction: Direction, distance: int = 1):
        coordinate = self.movement_strategy.move(self, grid, direction, distance)
        if coordinate is not None:
            self.coordinate = coordinate
        else:
            print("move failed")



