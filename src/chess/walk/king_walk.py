from chess.geometry.coordinate.coordinate import Coordinate
from chess.walk.knight_walk import KnightWalkException
from chess.walk.walk import Walk, DestinationUnreachableException
from chess.token.chess_piece import ChessPiece

class KingWalkException(DestinationUnreachableException):
    default_message = f"KingRank {DestinationUnreachableException.default_message}"

class KingWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holing KingRank
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        """
        A king moves horizontally and diagonally like a Queen but only in radius of 1
        """

        origin = chess_piece.coordinate_stack.current_coordinate()

        if not (
            abs(origin.row - destination.row) == 1 and
            abs(origin.column - destination.column) == 1
        ):
            raise KingWalkException(KnightWalkException.default_message)
        return True