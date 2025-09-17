from typing import Optional

from typing_extensions import TYPE_CHECKING

from chess.exception.stack_exception import (
    PushingNullEntityException,
    CorruptedStackException,
    DuplicatePushException
)

if TYPE_CHECKING:
    pass


class TeamList:
    _items: list['Team']
    _current_side: 'Team'

    def __init__(self):
        self._items = []
        self._current_side = self._items[-1] if self._items else None


    @property
    def items(self) -> list['Team']:
        """
        Returns a read-only view of the stack's contents. The returned sequence is safe to
        iterate and index, but mutating it will not affect the original stack.
        """

        return self._items


    @property
    def current_team(self) -> Optional['Team']:
        return self._items[-1] if self._items else None


    def is_empty(self) -> bool:
        return len(self._items) == 0


    def size(self) -> int:
        return len(self._items)


    def find_side_by_id(self, id: int) -> Optional['Team']:
        for side in self._items:
            if side.id == id:
                return side
        return None


    def push_side(self, side: 'Team'):
        method = "TeamStack.push_team"

        if side is None:
            raise PushingNullEntityException(f"{method}: {PushingNullEntityException.DEFAULT_MESSAGE}")

        if self._items is None:
            raise CorruptedStackException(f"{method}: {CorruptedStackException.DEFAULT_MESSAGE}")

        if self.current_team == side:
            raise DuplicatePushException(f"{method} {DuplicatePushException.DEFAULT_MESSAGE}")

        self._items.append(side)

