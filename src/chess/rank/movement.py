class MoveRule(ABC):
    @abstractmethod
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        pass


class VerticalMoveRule(MoveRule):
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same column, row changes
        return start.column == end.column and start.row != end.row


class HorizontalMoveRule(MoveRule):
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Same row, column changes
        return start.row == end.row and start.column != end.column


class DiagonalMoveRule(MoveRule):
    def is_valid(self, start: GridCoordinate, end: GridCoordinate) -> bool:
        # Row and column difference equal (non-zero)
        return abs(end.row - start.row) == abs(end.column - start.column) and start != end