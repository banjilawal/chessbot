from dataclasses import dataclass

from model.occupant.obstacle import Obstacle
from move.MovementController import MovementController
from move.board_direction import BoardDirection
from move.message_body import MessageBody


@dataclass(frozen=True)
class MovementQuery:
    requestor: Obstacle
    controller: MovementController
    query: MessageBody