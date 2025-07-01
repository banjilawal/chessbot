from dataclasses import dataclass

from model.occupant.obstacle import Obstacle
from travel.board_direction import BoardDirection


@dataclass(frozen=True)
class MessageBody:
    direction: BoardDirection
    distance: int