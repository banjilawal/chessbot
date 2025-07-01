from dataclasses import dataclass
from typing import List

from model.board.board import Board
from move.message_body import MessageBody


@dataclass
class MovementController:
    board: Board
    queries: List['MessageBody'] = tuple()

    def __str__(self):
        return f"MovementController(requestor={self.requestor}, direction={self.direction}, distance={self.distance})"