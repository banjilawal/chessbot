from dataclasses import dataclass, field
from typing import Optional, List, Union, Dict, TYPE_CHECKING

from common.dimension import Dimension
from common.direction import Direction
from model.grid_coordinate import GridCoordinate, CoordinateRange
from model.grid_entity import GridEntity
from strategy.horizontal_movement_strategy import HorizontalMovementStrategy

if TYPE_CHECKING:
    from model.board import Board


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

    def move(self, board: 'Board', destination_coordinate: GridCoordinate):
        if not self.movement_strategy.move(self, board, destination_coordinate):
            print(f"Failed to move {self.id} to {destination_coordinate}.")
        else :
            print(f"Moved {self.id} to {destination_coordinate}.")



