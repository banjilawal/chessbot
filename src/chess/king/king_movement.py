from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.search import SearchPattern
from chess.common.piece import Piece


class KingMovement(SearchPattern):
    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        pass

    def search(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        pass