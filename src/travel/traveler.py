from abc import ABC, abstractmethod

from model.board.grid_coordinate import Coordinate
from travel.bearing import Bearing
from travel.travel_decision import TravelDecision
from travel.travel_request import TravelRequest


class Traveler(ABC):
    """Interface for obstacles that can be moved."""

    @abstractmethod
    def traveler_id(self) -> int:

    # The coordinate is going to be the top-left coord.
    @abstractmethod
    def current_coordinate(self) -> Coordinate:

    @abstractmethod
    def send_travel_request(self, bearing: Bearing) -> TravelRequest:
        """Sends a travel request to the travel service."""
        pass

    @abstractmethod
    def accept_travel_decision(self, travel_decision: TravelDecision) -> bool:
        """Accepts the travel decision made by the travel service."""
        pass

    @abstractmethod
    def move(self, bearing: Bearing) -> bool:
        """Returns True if the obstacle is allowed to travel to the given cells."""
        pass
