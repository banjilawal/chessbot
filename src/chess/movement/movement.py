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
        if origin == destination:
            print("Cannot move if origin and destination are the same")
            return
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
    def __init__(self, origin: Coordinate, destination: Coordinate):
        super().__init__(origin, destination)

    def is_valid_move(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same column, row changes
        return origin.column == destination.column and origin.row != destination.row


class HorizontalMoveRule(MoveRule):
    """X changes while Y stays the same."""
    def __init__(self, origin: Coordinate, destination: Coordinate):
        super().__init__(origin, destination)

    def is_valid_move(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Same row, column changes
        return origin.row == destination.row and origin.column != destination.column


class DiagonalMoveRule(MoveRule):
    """
    A DiagonalMoveRule is a rule that defines a diagonal movement. Diagonal movement is:
    forward Xj, Yj <= Xi, Yi = Xi-1, Yi+1
    backward Xj, Yj>=Xi, Yi = Xi+1, Yi+1
    """
    def is_valid_move(self, origin: Coordinate, destination: Coordinate) -> bool:
        # Row and column difference equal (non-zero)
        return (
            origin != destination and
                abs(origin.row - destination.row) == abs(destination.column - origin.column)
        )


