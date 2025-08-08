from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.line.diagonal import Diagonal
from chess.motion.walk.walk import Walk
from chess.team.element.piece import ChessPiece


class BishopWalk(Walk):

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:

        return Diagonal.is_diagonal(
            chess_piece.coordinate_stack.current_coordinate(),
            destination
        )