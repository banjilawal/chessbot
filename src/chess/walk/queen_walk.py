from typing import Optional

from chess.board.board import ChessBoard
from chess.geometry.coordinate.coordinate import Coordinate
from chess.walk.bishop_walk import BishopWalk
from chess.walk.castle_walk import CastleWalk
from chess.walk.walk import Walk, WalkException
from chess.token.chess_piece import ChessPiece

class QueenWalkException(WalkException):
    default_message = f"QueenRank {WalkException.default_message}"

class QueenWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece with QueenRank
    """

    @staticmethod
    def is_walkable(
        chess_piece: ChessPiece,
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