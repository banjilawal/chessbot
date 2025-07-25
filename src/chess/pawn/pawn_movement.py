from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.vertical_pattern import VerticalPatern
from chess.motion.movement import MovementStrategy
from chess.common.piece import Piece


class PawnMovement(MovementStrategy):
    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        pass

    def __init__(self, motion_definitions=[VerticalPatern, DiagonalPattern]):
        super().__init__(motion_definitions)

    def possible_destinations(self, origin: Coordinate, board: Board,) -> list[Coordinate]:
        destinations = []
        next_point = origin.shift(0, 1)
        if board.coordinate_is_valid(next_point):
            destinations.append(next_point)
        return destinations
