from collections.abc import Sequence
from typing import List, Optional

from chess.exception.stack import CorruptedStackException, PushingNullEntityException, DuplicatePushException, \
    PopEmptyStackException
from chess.geometry.coord import Coord


class CoordStack:
    _items: list[Coord]
    _current_coord: [Coord]

    def __init__(self):
        self._items = []
        self._current_coord = self._items[-1] if self._items else None

    @property
    def items(self) -> Sequence[Coord]:
        return self._items.copy()

    @property
    def current_coord(self) -> Optional[Coord]:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def push_coord(self, coord):
        method_name = "CoordStack.push"

        if coord is None:
            raise PushingNullEntityException(
                f"{method_name}: {PushingNullEntityException.DEFAULT_MESSAGE}"
            )

        if self._items is None:
            raise CorruptedStackException(f"{method_name}: {CorruptedStackException.DEFAULT_MESSAGE}")

        if self.current_coord == coord:
            raise DuplicatePushException(
                f"{method_name}: {DuplicatePushException.DEFAULT_MESSAGE}"
            )
        self._items.append(coord)

    def undo_push(self):
        method_name = "CoordStack.undo_push"

        if len(self._items) == 0:
            raise PopEmptyStackException(f"{method_name}: {PopEmptyStackException.DEFAULT_MESSAGE}")
        self._items.pop()
#
#
# def main():
#     coord_stack = CoordStack()
#     coord_stack.push_coord(Coord(1, 1))
#     coord_stack.push_coord(Coord(1, 1))
#     print(f"Current Coord: {coord_stack.current_coord}")
#     coord_stack.undo_push()
#     print(f"Current Coord after undo: {coord_stack.current_coord}")
#
#
# if __name__ == '__main__':
#     main()