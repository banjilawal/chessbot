from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.definition.diagonal import DiagonalDefinition
from chess.motion.definition.vertical import VerticalDefinition
from chess.motion.movement.movement import MovementStrategy


class PawnMovement(MovementStrategy):
    def __init__(self, motion_definitions=[VerticalDefinition, DiagonalDefinition]):
        super().__init__(motion_definitions)

    def possible_destinations(self, origin: Coordinate, board: Board,) -> list[Coordinate]:
        destinations = []
        next_point = origin.shift(0, 1)
        if board.coordinate_is_valid(next_point):
            destinations.append(next_point)
        return destinations
