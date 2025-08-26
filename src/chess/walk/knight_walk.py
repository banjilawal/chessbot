from chess.geometry.coordinate.coord import Coordinate
from chess.walk.walk import Walk, WalkException
from chess.token.piece import ChessPiece

class KnightWalkException(WalkException):
    default_message = f"KnightRank {WalkException.default_message}"

class KnightWalk(Walk):
    """
    Implementation of Walk interface for ChessPiece with QueenRank
    """


    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:

        # Uses difference between the origin and destination rows and columns to
        # see if they form an L shaped motion.

        origin = chess_piece.positions.current_coordinate()

        row_diff = abs(origin.row - destination.row)
        col_diff = abs(origin.column - destination.column)

        # A KnightRank's move is always (2,1) or (1,2) in terms of row/column difference
        if not (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            raise KnightWalkException(KnightWalkException.default_message)
        return True