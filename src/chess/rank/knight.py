from typing import List, Optional

from chess.geometry.board import Board
from chess.common.geometry import Quadrant, Coordinate
from chess.common.piece import Piece
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank import Rank


class Knight(Rank):
    def __init__(
        self,
        name: str,
        value,
        quadrants: List[Quadrant],
        members: List[Piece],
    ):
        super.__init__(name, value, quadrants, members)

    def move(self, piece: Piece, board: Board, destination: Coordinate) -> Optional[TurnRecord]:
        pass

    def walk(self) -> List[Coordinate]:
        pass

    def search_pattern(self) -> List[Coordinate]:
        pass

    def explore(self, piece: Piece, board: Board):
        pass

    def select_destination(self):
        pass