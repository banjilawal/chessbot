from dataclasses import dataclass

from travel.travel_request import TravelRequest


@dataclass(frozen=True)
class TravelDecision:
    original_request: TravelRequest
    distance_granted: int