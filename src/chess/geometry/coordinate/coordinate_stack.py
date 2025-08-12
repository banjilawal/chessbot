from typing import Optional, List

from chess.exception.exception import ChessException
from chess.geometry.coordinate.coordinate import Coordinate


class PopEmptyCoordinateStackException(ChessException):
    default_message = "Cannot pop from empty coordinate stack"

class PushNullCoordinateException(ChessException):
    default_message = "Cannot push p null coordinate on to te stack"

class CoordinateStack:
    _stack: List[Coordinate]

    def __init__(self):
        self._stack = []

    @property
    def stack(self) -> List[Coordinate]:
        return self._stack

    def is_empty(self) -> bool:
        return self.size() == 0 and self.current_coordinate() is None


    def size(self) -> int:
        return len(self._stack)


    def current_coordinate(self) -> Optional[Coordinate]:
        return self._stack[-1] if self._stack else None


    def push_coordinate(self, coordinate):
        method_name = "CoordinateStack.push"

        if self.current_coordinate() != coordinate:
            self._stack.append(coordinate)

    def undo_push(self):
        if self.size() == 0:
            raise PopEmptyCoordinateStackException("Cannot pop from empty coordinate stack")

        self._stack.pop()