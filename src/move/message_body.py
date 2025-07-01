from dataclasses import dataclass

from model.occupant.obstacle import Obstacle
from move.board_direction import BoardDirection


@dataclass(frozen=True)
class MessageBody:
    direction: BoardDirection
    distance: int