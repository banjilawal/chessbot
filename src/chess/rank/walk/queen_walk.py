from chess.geometry.coordinate.coordinate import Coordinate
from chess.rank.walk.bishop_walk import BishopWalk
from chess.rank.walk.castle_walk import CastleWalk
from chess.rank.walk.walk import Walk
from chess.token.chess_piece import ChessPiece


class QueenWalk(Walk):

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:

        return (
            CastleWalk.is_walkable(chess_piece, destination) or
            BishopWalk.is_walkable(chess_piece, destination)
        )