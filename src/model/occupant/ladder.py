from dataclasses import dataclass

from model.board.grid_coordinate import GridCoordinate
from model.occupant.occupant import Occupant
from travel.bearing import Bearing
from travel.travel_decision import TravelDecision
from travel.travel_request import TravelRequest
from travel.traveler import Traveler


@dataclass
class Ladder(Occupant, Traveler):

    def id(self) -> int:
        return super().id

    def send_travel_request(self, bearing: Bearing) -> TravelRequest:
        pass

    def accept_travel_decision(self, travel_decision: TravelDecision) -> bool:
        pass

    def move(self, bearing: Bearing) -> bool:
        pass

