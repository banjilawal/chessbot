from dataclasses import dataclass
from typing import Optional

from src.common.dimension import Dimension
from src.model.board.grid_coordinate import GridCoordinate
from src.model.occupant.occupant import Occupant
from src.travel.bearing import Bearing
from src.travel.travel_decision import TravelDecision
from src.travel.travel_request import TravelRequest
from src.travel.traveler import Traveler


@dataclass
class Crate(Occupant):

    def __init__(self, id: int, height: int, coordinate: Optional[GridCoordinate] = None):
        super().__init__(id=id, dimension=Dimension(length=1, height=height), coordinate=coordinate)

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

