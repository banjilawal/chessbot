from typing import Optional

from assurance.transaction_result import TransactionReport, StatusCode
from chess.common.exceptions import ChessException
from chess.geometry.board.coordinate_validator import CoordinateValidator
from chess.geometry.board.coordinate import Coordinate
from chess.transaction.failure import Failure

class PopEmptyCoordinateStackException(ChessException):
    default_message = "Cannot pop from empty coordinate stack"
class PushNullCoordinateException(ChessException):
    default_message = "Cannot push a null coordinate on to te stack"

class CoordinateStack:
    def __init__(self):
        _stack: [Coordinate] = []

    def is_empty(self) -> bool:
        return self.size() == 0 and self.current_coordinate() is None


    def size(self) -> int:
        return len(self._stack)


    def current_coordinate(self) -> Optional[Coordinate]:
        return self._stack[-1] if self._stack else None


    def push_coordinate(self, coordinate) -> TransactionReport:
        method_name = "CoordinateStack.push"
        test_report = CoordinateValidator.test_not_none(coordinate)
        if test_report.payload is None:
            raise test_report.validation_exception
            # return OldTransactionResult(method_name,  test_report.validation_exception)

        destination = test_report.payload
        source = self.current_coordinate()

        if source != destination:
            self._stack.append(destination)

        return TransactionReport(method_name, StatusCode.SUCCESS)

    def undo_push(self) -> TransactionReport:
        if self.size() == 0:
            raise PopEmptyCoordinateStackException("Cannot pop from empty coordinate stack")

        self._stak.pop()
        return TransactionReport("CoordinateStack.undo_push", StatusCode.SUCCESS)
    #
    #
    #
    # # === Stack operations ===
    # def push_new_coordinate(self, coordinate: Coordinate) -> TransactionReport:
    #     method = "ChessPiece.push_new_coordinate"
    #     old_size = len(self._coordinate_stack)
    #
    #     if coordinate is None:
    #         return TransactionReport(method, Failure("Cannot push a null coordinate on to te stack"))
    #     if coordinate in self._coordinate_stack:
    #         print(f"{coordinate} is already on {self._label}'s stack. No need for a push.")
    #         return TransactionReport(method, StatusCode.SUCCESS)
    #
    #     self._coordinate_stack.append(coordinate)
    #
    #     if coordinate == self.current_coordinate() and old_size + 1 == len(self._coordinate_stack):
    #         return TransactionReport(method, StatusCode.SUCCESS)
    #     return TransactionReport(method, Failure("Failed to push coordinate on to stack"))
    #
    #
    # def undo_last_coordinate_push(self) -> Optional[Coordinate]:
    #
    #     if len(self._coordinate_stack) == 0:
    #         print(f"{self._label} has no coordinates to undo")
    #         return None
    #
    #     if self._coordinate_stack:
    #         return self._coordinate_stack.pop()
    #     return None
    #
    #
    # def current_coordinate(self) -> Optional[Coordinate]:
    #     return self._coordinate_stack[-1] if self._coordinate_stack else None