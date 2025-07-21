from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from geometry import GridCoordinate

if TYPE_CHECKING:
    from chess.chess_piece.piece import ChessPiece
    from board import Board

class MoveRule(ABC):
    @abstractmethod
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        pass


class VerticalMoveRule(MoveRule):
    """Y changes while X stays the same."""
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same column, row changes
        return start.column == end.column and start.row != end.row


class HorizontalMoveRule(MoveRule):
    """X changes while Y stays the same."""
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same row, column changes
        return start.row == end.row and start.column != end.column


class DiagonalMoveRule(MoveRule):
    """
    A DiagonalMoveRule is a rule that defines a diagonal movement. Diagonal movement is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Row and column difference equal (non-zero)
        return abs(end.row - start.row) == abs(end.column - start.column) and start != end

class MovementStrategy(ABC):
    """ A MovementStrategy is a collection of MoveRules that define how a piece can move."""
    def __init__(self, rules: list[MoveRule]):
        self.rules = rules

    def is_valid_move(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        return any(rule.is_valid(start, end) for rule in self.rules)

    def _check_basic_conditions(self, chess_piece: ChessPiece, board: 'Board', destination_coordinate: 'GridCoordinate') -> bool:
        if chess_piece is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] Board cannot be None. Cannot move.")
            return False
        if chess_piece.top_left_coordinate is None:
            print("[Warning] Mover has no top_left_coordinate. Cannot move.")
            return False
        if destination_coordinate is None:
            print("[Warning] Destination top_left_coordinate cannot be None. Cannot move.")
            return False
        if destination_coordinate.column < 0 or destination_coordinate.column >= board.dimension.length:
            print(f"[Warning] Horizontal move out of bounds: {destination_coordinate.column}")
            return False
        if destination_coordinate.row < 0 or destination_coordinate.row >= board.dimension.length:
            print(f"[Warning] Vertical move out of bounds: {destination_coordinate.row}")
            return False
        return True

    @abstractmethod
    def move(self, mover: 'Mover', board: 'Board', destination_coordinate: 'GridCoordinate') -> bool:
        """Perform the move if valid. Return True if successful, False otherwise."""
        pass

class PawnMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement pawn-specific movement logic
        return False


class KnightMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement knight's L-shaped movement
        return False


class BishopMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement bishop's diagonal movement
        return False


class CastleMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement rook's straight-line movement
        return False


class QueenMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement queen's combined rook + bishop movement
        return False


class KingMovement(MovementStrategy):
    def move(self, chess_piece: 'ChessPiece', board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        # TODO: Implement king's single-step any direction, and castling
        return False
