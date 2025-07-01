from dataclasses import dataclass

from travel.bearing import Bearing

@dataclass(frozen=True)
class TravelRequest:
    request_id: int
    traveller_id: int
    bearing: Bearing