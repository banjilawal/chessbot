from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.horizontal_pattern import HorizontalPattern
from chess.motion.logic.vertical import VerticalDefinition
from chess.motion.movement.movement import MovementStrategy
from chess.motion.quadrant import Quadrant
from chess.motion.walks import linear_walk
from chess.piece.piece import Piece


class CastleMovement(MovementStrategy):
    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def path_exists(self, origin: Coordinate, destination: Coordinate, board: Board) -> Optional[GeometryPattern]:
        pass

    def __init__(self, motion_definitions=[HorizontalPattern, VerticalDefinition]):
        super().__init__(motion_definitions)

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.N, Quadrant.E, Quadrant.S, Quadrant.W]:
            destinations.extend(linear_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations