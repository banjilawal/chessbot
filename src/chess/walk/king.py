from chess.geometry.coordinate.coord import Coordinate
from chess.walk.knight import KnightWalkException
from chess.walk.base import Walk, WalkException
from chess.token.model import Piece

class KingWalkException(WalkException):
    default_message = f"KingRank {WalkException.default_message}"

class KingWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holing KingRank
    """

    @staticmethod
    def is_walkable(chess_piece: Piece, destination: Coordinate) -> bool:
        """
        A king moves horizontally and diagonally like a Queen but only in radius of 1
        """

        origin = chess_piece.positions.current_coordinate()

        if not (
            abs(origin.row - destination.row) == 1 and
            abs(origin.column - destination.column) == 1
        ):
            raise KingWalkException(KnightWalkException.default_message)
        return True