from typing import Optional

from assurance.result import Result, OperationStatus
from assurance.transaction_report import TransactionReport
from chess.common.exceptions import ChessException
from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.coordinate.coordinate_validator import CoordinateValidator


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

        return TransactionReport(method_name, Result(OperationStatus.SUCCESS))

    def undo_push(self) -> TransactionReport:
        if self.size() == 0:
            raise PopEmptyCoordinateStackException("Cannot pop from empty coordinate stack")

        self._stak.pop()
        return TransactionReport("CoordinateStack.undo_push", Result(OperationStatus.SUCCESS))