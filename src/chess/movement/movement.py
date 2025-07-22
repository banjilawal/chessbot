from abc import ABC, abstractmethod

from chess.common.geometry import Coordinate


class MoveRule(ABC):
    origin: Coordinate
    destination: Coordinate
    
    def __self__(self, origin: Coordinate, destination: Coordinate):
        if origin is None:
            raise ValueError("Origin cannot be None")
        if destination is None:
            raise ValueError("Destination cannot be None")
        self._origin = origin
        self._destination = destination


    @property
    def origin(self) -> Coordinate:
        return self._origin


    @property
    def destination(self) -> Coordinate:
        return self._destination


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, MoveRule):
            return False
        return self.origin == other.origin and self.destination == other.destination


    def __hash__(self):
        return hash((self.origin, self.destination))


    @abstractmethod
    def is_valid_move(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass

class VerticalMoveRule(MoveRule):
    """Y changes while X stays the same."""
    def is_valid_move(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same column, row changes
        return start.column == end.column and start.row != end.row

class HorizontalMoveRule(MoveRule):
    """X changes while Y stays the same."""
    def is_valid_move(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same row, column changes
        return start.row == end.row and start.column != end.column


class DiagonalMoveRule(MoveRule):
    """
    A DiagonalMoveRule is a rule that defines a diagonal movement. Diagonal movement is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """
    def is_valid_move(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Row and column difference equal (non-zero)
        return abs(end.row - start.row) == abs(end.column - start.column) and start != end


