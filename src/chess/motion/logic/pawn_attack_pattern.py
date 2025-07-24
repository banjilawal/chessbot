from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.piece.promotable import Pawn


class PawnAttackPattern:

    @staticmethod
    def matches(pawn: Pawn, destination: Coordinate, board: Board) -> bool:
        if pawn is None or board is None:
            return False

        origin = pawn.current_position()
        if origin is None or not board.coordinate_is_valid(destination):
            return False

        row_diff = destination.row - origin.row
        col_diff = abs(destination.column - origin.column)

        if row_diff != 1 or col_diff != 1:
            return False

        target = board.get_chess_piece_by_coordinate(destination)
        if target is None:
            return False

        return pawn.is_enemy(target)