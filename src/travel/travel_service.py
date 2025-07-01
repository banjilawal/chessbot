from dataclasses import dataclass, field
from typing import List

from common.game_default import GameDefault
from model.board.board import Board
from model.occupant.traveler import Traveler
from travel.bearing import Bearing
from travel.travel_decision import TravelDecision
from travel.travel_request import TravelRequest


@dataclass
class TravelService:
    id: int
    board: Board
    queue: List[TravelRequest] = field(default_factory=list)

    def create_request(self, traveller: Traveler, bearing: Bearing) -> TravelRequest:
        request = TravelRequest(
            request_id=len(self.queue) + 1,
            traveller_id=traveller.id,
            bearing=bearing
        )
        self.enqueue_request(request)
        return request

    def enqueue_request(self, request: TravelRequest):
        self.queue.append(request)

    def give_decision(self) -> TravelDecision:
        request = self.queue.pop(0)
        return self.apply_rules(request)

    def apply_rules(self, request: TravelRequest) -> TravelDecision:
        return TravelDecision(original_request=request, distance_granted=0)




