from typing import Optional

from chess.board.board import ChessBoard
from chess.geometry.coordinate.coord import Coordinate
from chess.walk.bishop import BishopWalk
from chess.walk.castle import CastleWalk
from chess.walk.base import Walk, WalkException
from chess.token.model import Piece

class QueenWalkException(WalkException):
    default_message = f"QueenRank {WalkException.default_message}"

class QueenWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece with QueenRank
    """

    @staticmethod
    def is_walkable(
        chess_piece: Piece,
        destination: Coordinate,
    ) -> bool:
        # Queen movement combines Rook and Bishop movement.
        # Return true if chess_piece wants to move either way.

        if not (
            CastleWalk.is_walkable(chess_piece, destination) or
            BishopWalk.is_walkable(chess_piece, destination)
        ):
            raise QueenWalkException(QueenWalkException.default_message)
        return True