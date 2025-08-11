
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.horizontal import Horizontal
from chess.geometry.line.vertical import Vertical
from chess.walk.walk import Walk
from chess.token.chess_piece import ChessPiece


class CastleWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holding CastleRank
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        """
        Uses chess.geometry.line.Vertical and chess.geometry.line.Horizontal to
        test if Castle can legally reach the destination.
        """

        origin = chess_piece.coordinate_stack.current_coordinate()

        return (
            Vertical.is_vertical(origin, destination) or
            Horizontal.is_horizontal(origin, destination)
        )
