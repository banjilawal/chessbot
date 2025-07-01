from dataclasses import dataclass

from common.game_default import GameDefault
from travel.board_direction import BoardDirection


@dataclass(frozen=True)
class Bearing:
    direction: BoardDirection
    distance: int = GameDefault.MAX_TRAVEL_DISTANCE