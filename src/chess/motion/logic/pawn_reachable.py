from chess.geometry.coordinate import Coordinate
from chess.motion.logic.reachable import Reachable
from chess.piece.piece import Piece


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
    def can_advance(pawn: Piece, destination: Coordinate) -> bool:
        """
        Check if pawn can advance to destination (forward movement).
        Handles first move (1 or 2 squares) vs subsequent moves (1 square only).
        """
        if pawn is None:
            return False

        origin = pawn.current_position()
        if origin is None:
            return False

        position_history = pawn.position_history
        if len(position_history) == 0 or position_history is None:
            return False

        # Must be same column (straight forward)
        if origin.column != destination.column:
            return False

        row_diff = destination.row - origin.row

        # First move: can advance 1 or 2 squares
        if len(position_history) == 1:
            return row_diff in (1, 2)
        # Subsequent moves: can only advance 1 square
        else:
            return row_diff == 1

    @staticmethod
    def can_attack(pawn: Piece, destination: Coordinate, board: Board) -> bool:
        """
        Check if pawn can attack destination (diagonal capture).
        Requires enemy piece at destination.
        """
        if pawn is None or board is None:
            return False

        origin = pawn.current_position()
        if origin is None or not board.coordinate_is_valid(destination):
            return False

        row_diff = destination.row - origin.row
        col_diff = abs(destination.column - origin.column)

        # Must be diagonal (1 square forward, 1 square sideways)
        if row_diff != 1 or col_diff != 1:
            return False

        # Must have enemy piece at destination
        target = board.get_chess_piece_by_coordinate(destination)
        if target is None:
            return False

        return pawn.is_enemy(target)