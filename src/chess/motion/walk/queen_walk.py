from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.map_service import MapService
from chess.motion.walk.bishop_walk import BishopWalk
from chess.motion.walk.castle_walk import CastleWalk
from chess.geometry.line.diagonal import Diagonal
from chess.motion.walk.walk import Walk
from chess.team.element.piece import ChessPiece


class QueenWalk(Walk):

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate, map_service: MapService) -> bool:

        return (
            CastleWalk.is_walkable(chess_piece, destination) or
            BishopWalk.is_walkable(chess_piece, destination)
        )