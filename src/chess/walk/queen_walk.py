from chess.geometry.coordinate.coordinate import Coordinate
from chess.walk.bishop_walk import BishopWalk
from chess.walk.castle_walk import CastleWalk
from chess.walk.walk import Walk
from chess.token.chess_piece import ChessPiece


class QueenWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece with QueenRank
    """

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        # Queen movement combines Rook and Bishop movement.
        # Return true if chess_piece wants to move either way.

        return (
            CastleWalk.is_walkable(chess_piece, destination) or
            BishopWalk.is_walkable(chess_piece, destination)
        )