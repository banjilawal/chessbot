from typing import Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.logic.geomtery_pattern import GeometryPattern
from chess.motion.logic.diagonal_pattern import DiagonalPattern
from chess.motion.quadrant import Quadrant
from chess.motion.movement import MovementStrategy
from chess.motion.walks import diagonal_walk
from chess.common.piece import Piece


class BishopMovement(MovementStrategy):
    def __init__(self, motion_definitions=[DiagonalPattern]):
        super().__init__(motion_definitions)

    def path_exists(self, origin: Coordinate, destination: Coordinate) -> bool:
        return DiagonalPattern.points_match_pattern(origin, destination)

    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        pass

    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        destinations = []
        for quadrant in [Quadrant.NE, Quadrant.SW, Quadrant.SE, Quadrant.NW]:
            destinations.extend(diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations






