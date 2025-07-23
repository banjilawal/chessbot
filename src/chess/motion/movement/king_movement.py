from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.motion.movement.movement import MovementStrategy


class KingMovement(MovementStrategy):
    def possible_destinations(self, origin: Coordinate, board: Board) -> list[Coordinate]:
        pass