from chess.board.chess_board import ChessBoard
from chess.common.geometry import Coordinate
from chess.motion.motions.diagonal import DiagonalMotion
from chess.motion.quadrant import Quadrant
from chess.motion.strategy.movement_strategy import MovementStrategy


class BishopMovement(MovementStrategy):

    def __init__(self, rules=[DiagonalMotion]):
        super().__init__(rules)


    def possible_destinations(self, origin: Coordinate, board: ChessBoard) -> list[Coordinate]:
        destinations = []
        for quadrant in Quadrant:
            destinations.append(self._diagonal_walk(origin, quadrant.x_delta, quadrant.y_delta, board))
        return destinations


    def _diagonal_walk(
            self,
            origin: Coordinate,
            x_delta: int,
            y_delta: int,
            board: ChessBoard
   ) -> list[Coordinate]:
        destinations = []
        current = origin.shift(x_delta, y_delta)

        while board.is_valid_coordinate(current):
            occupant = board.get_chess_piece_by_coordinate(current)
            if occupant is None:
                destinations.append(current)
            else:
                break
            current = current.shift(x_delta, y_delta)
        return destinations