from chess.geometry.coordinate.coordinate import Coordinate
from chess.rank.walk.walk import Walk
from chess.token.chess_piece import ChessPiece


class KingWalk(Walk):

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        origin = chess_piece.coordinate_stack.current_coordinate()

        return (
            abs(origin.row - destination.row) == 1 and
            abs(origin.column - destination.column) == 1
        )