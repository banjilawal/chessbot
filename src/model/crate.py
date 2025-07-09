from dataclasses import dataclass
from typing import Optional

from src.common.dimension import Dimension
from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity


@dataclass
class Crate(GridEntity):

    def __init__(self, crate_id: int, length: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=crate_id, dimension=Dimension(length=length, height=1), coordinate=coordinate)

    def move_left(self, distance: int):
        new_coordinate = GridCoordinate(row=self.coordinate.row, column=self.coordinate.column - distance)
        self.coordinate = new_coordinate

    def move_right(self, distance: int):
        new_coordinate = GridCoordinate(row=self.coordinate.row, column=self.coordinate.column + distance)
        self.coordinate = new_coordinate


    # def id(self) -> int:
    #     return super().id
    #
    # def send_travel_request(self, bearing: Bearing) -> TravelRequest:
    #     pass
    #
    # def accept_travel_decision(self, travel_decision: TravelDecision) -> bool:
    #     pass
    #
    # def move(self, bearing: Bearing) -> bool:
    #     pass

