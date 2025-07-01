from dataclasses import dataclass

from common.game_default import GameDefault
from model.occupant.obstacle import Obstacle
from travel.travel_service import MovementController
from travel.board_direction import BoardDirection
from travel.message_body import MessageBody


@dataclass(frozen=True)
class TravelRequest:
    requestor: Obstacle
    controller: MovementController
    direction: BoardDirection
    distance: int = GameDefault.MAX_TRAVEL_DISTANCE