from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.movement.movement import MovementStrategy
from chess.piece.piece import Piece


class KingMovement(MovementStrategy):
    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        pass

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        pass