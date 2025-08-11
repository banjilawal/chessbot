from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.walk.walk import Walk
from chess.token.chess_piece import ChessPiece


class BishopWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece holding BishopRank
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:

        """
        Uses chess.geometry.line.Diagonal to test if Bishop can legally reach the destination.
        """

        return Diagonal.is_diagonal(
            chess_piece.coordinate_stack.current_coordinate(),
            destination
        )