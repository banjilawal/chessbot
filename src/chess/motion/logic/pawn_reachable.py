from chess.geometry.board import ChessBoard
from chess.geometry.board.coordinate import Coordinate
from chess.geometry.diagonal import Diagonal
from chess.geometry.vertical import Vertical
from chess.motion.logic.reachable import Reachable
from chess.piece.piece import ChessPiece
from chess.rank.pawn import Pawn


class PawnReachable(Reachable):
    """
    Consolidated pawn movement validation with specialized static methods
    for different movement types.
    """

    @staticmethod
    def is_reachable(origin: Coordinate, destination: Coordinate) -> bool:
        """
        Basic geometric reachability - maintains Reachable interface.
        Only checks if destination is geometrically reachable by pawn movement.
        """
        row_diff = destination.row - origin.row
        col_diff = abs(destination.column - origin.column)

        # Forward move (1 or 2 squares)
        if origin.column == destination.column:
            return row_diff in (1, 2)

        # Diagonal move (1 square)
        if col_diff == 1:
            return row_diff == 1

        return False

    @staticmethod
    def can_advance(pawn: ChessPiece, destination: Coordinate) -> bool:
        if pawn is None:
            return False

        if not isinstance(pawn.rank, Pawn):
            return False

        origin = pawn.current_coordinate()
        if origin is None:
            return False

        position_history = pawn.position_history
        if len(position_history) == 0 or position_history is None:
            return False

        if not Vertical.is_vertical(origin, destination):
            return False

        row_diff = destination.row - origin.row
        if len(position_history) == 1:
            return row_diff in (1, 2)
        else:
            return row_diff == 1

    @staticmethod
    def can_attack(pawn: ChessPiece, destination: Coordinate, board: ChessBoard) -> bool:
        if pawn is None or board is None:
            return False

        if not isinstance(pawn.rank, Pawn):
            return False

        origin = pawn.current_coordinate()
        if origin is None or not board.coordinate_is_valid(destination):
            return False

        if not Diagonal.is_diagonal(origin, destination) or  not (destination.row - origin.row) == 1:
            return False

        target = board.find_chess_piece(destination)
        if target is None:
            return False

        return pawn.is_enemy(target)