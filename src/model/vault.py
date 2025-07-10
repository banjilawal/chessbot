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

    def move_left(self, distance: int):
        if distance < 0:
            print("Distance to move must be positive")
            return
        if self.coordinate is None:
            print("Coordinate is null. Cannot move left without coordinate")
        destination_coordinate = GridCoordinate(row=self.coordinate.row, column=self.coordinate.column - distance)
        self.coordinate = destination_coordinate

    def move_right(self, distance: int):
        if distance < 0:
            print("Distance to move must be positive")
            return
        if self.coordinate is None:
            print("Coordinate is null. Cannot move left without coordinate")
        destination_coordinate = GridCoordinate(row=self.coordinate.row, column=self.coordinate.column + distance)
        self.coordinate = destination_coordinate




