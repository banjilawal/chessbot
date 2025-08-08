from chess.geometry.coordinate.coordinate import Coordinate
from chess.motion.walk.walk import Walk
from chess.team.model.piece import ChessPiece


class KnightWalk(Walk):

    @staticmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        origin = chess_piece.coordinate_stack.current_coordinate()

        row_diff = abs(origin.row - destination.row)
        col_diff = abs(origin.column - destination.column)

        # A KnightMotionController's move is always (2,1) or (1,2) in terms of row/column difference
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)