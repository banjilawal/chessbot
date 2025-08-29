
from chess.geometry.coordinate.coord import Coordinate
from chess.geometry.line.horizontal import Horizontal
from chess.geometry.line.vertical import Vertical
from chess.walk.base import Walk, WalkException
from chess.token.model import Piece

class CastleWalkException(WalkException):
    default_message = f"CastleRank {WalkException.default_message}"

class CastleWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holding CastleRank
    """

    @staticmethod
    def is_walkable(chess_piece: Piece, destination: Coordinate) -> bool:
        """
        Uses chess.geometry.line.Vertical and chess.geometry.line.Horizontal to
        test if Castle can legally reach the destination.
        """

        origin = chess_piece.positions.current_coordinate()

        if (
            Vertical.is_vertical(origin, destination) or
            Horizontal.is_horizontal(origin, destination)
        ):
            raise CastleWalkException(CastleWalkException.default_message)
        return True
