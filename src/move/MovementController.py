from dataclasses import dataclass
from typing import List

from model.board.board import Board
from move.movement_query import MovementQuery


@dataclass
class MovementController:
    board: Board
    queries: List['MovementQuery'] = tuple()
