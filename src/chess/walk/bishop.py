from chess.geometry.coordinate.coord import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.walk.base import Walk, WalkException
from chess.token.model import ChessPiece

class BishopWalkException(WalkException):
    default_message = f"BishopRank {WalkException.default_message}"

class BishopWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holding BishopRank
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:

        """
        Uses chess.geometry.line.Diagonal to test if Bishop can legally reach the destination.
        """

        if Diagonal.is_diagonal(
            chess_piece.positions.current_coordinate(),
            destination
        ):
            raise BishopWalkException(BishopWalkException.default_message)
        return True
