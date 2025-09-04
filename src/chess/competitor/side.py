from collections.abc import Sequence
from typing import Optional, List

from typing_extensions import TYPE_CHECKING

from chess.exception.stack import (
    PushingNullEntityException,
    CorruptedStackException,
    DuplicatePushException
)

if TYPE_CHECKING:
    from chess.side.model import Side


class SideRecord:
    _items: list['Side']
    _current_side: 'Side'

    def __init__(self):
        self._items = []
        self._current_side = self._items[-1] if self._items else None


    @property
    def items(self) -> list['Side']:
        """
        Returns a read-only view of the stack's contents. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original stack.
        """

        return self._items


    @property
    def current_side(self) -> Optional['Side']:
        return self._items[-1] if self._items else None


    def is_empty(self) -> bool:
        return len(self._items) == 0


    def size(self) -> int:
        return len(self._items)


    def find_side_by_id(self, id: int) -> Optional['Side']:
        for side in self._items:
            if side.id == id:
                return side
        return None


    def push_side(self, side: 'Side'):
        method = "TeamStack.push_team"

        if side is None:
            raise PushingNullEntityException(f"{method}: {PushingNullEntityException.DEFAULT_MESSAGE}")

        if self._items is None:
            raise CorruptedStackException(f"{method}: {CorruptedStackException.DEFAULT_MESSAGE}")

        if self.current_side == side:
            raise DuplicatePushException(f"{method} {DuplicatePushException.DEFAULT_MESSAGE}")

        self._items.append(side)

