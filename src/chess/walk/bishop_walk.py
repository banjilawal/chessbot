from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.walk.walk import Walk, DestinationUnreachableException
from chess.token.chess_piece import ChessPiece

class BishopWalkException(DestinationUnreachableException):
    default_message = f"BishopRank {DestinationUnreachableException.default_message}"

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
            chess_piece.coordinate_stack.current_coordinate(),
            destination
        ):
            raise BishopWalkException(BishopWalkException.default_message)
        return True
