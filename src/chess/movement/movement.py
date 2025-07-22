from abc import ABC, abstractmethod

from chess.common.geometry import Coordinate


class MoveRule(ABC):
    __
    @abstractmethod
    def is_valid(self, start: Coordinate, end: Coordinate) -> bool:
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


