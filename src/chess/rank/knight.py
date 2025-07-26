from typing import List, Optional

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.piece.piece import Piece
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank import Rank


class Knight(Rank):
    def __init__(self, name: str, acronym: str, capture_value: int, territories: List[Quadrant]):
        super().__init__(name, acronym, capture_value, territories)

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