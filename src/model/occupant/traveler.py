from abc import ABC, abstractmethod
from typing import List

from travel.bearing import Bearing
from travel.board_direction import BoardDirection
from src.model.cell.cell import Cell
from travel.travel_decision import TravelDecision
from travel.travel_request import TravelRequest


class Traveler(ABC):
    """Interface for obstacles that can be moved."""

    @abstractmethod
    def traveler_id(self) -> int:

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
