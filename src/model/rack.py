from dataclasses import dataclass
from typing import Optional

from common.dimension import Dimension
from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity


@dataclass
class Rack(GridEntity):

    def __init__(self, rack_id: int, height: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=rack_id, dimension=Dimension(length=1, height=height), coordinate=coordinate)

    def move_up(self, distance: int):
        new_coordinate = GridCoordinate(row=self.coordinate.row - distance, column=self.coordinate.column)
        self.coordinate = new_coordinate

    def move_down(self, distance: int):
        new_coordinate = GridCoordinate(row=self.coordinate.row + distance, column=self.coordinate.column)
        self.coordinate = new_coordinate
