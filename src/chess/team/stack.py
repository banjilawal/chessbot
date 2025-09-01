from typing import Optional, List

from chess.exception.stack import PushingNullEntityException, CorruptedStackException, DuplicatePushException
from chess.team.model import Team


class TeamStack:
    _items: List[Team]
    _current_team: [Team]

    def __init__(self):
        self._items = []
        self._current_team = self._items[-1] if self._items else None

    @property
    def items(self) -> List[Team]:
        return self._items.copy()

    @property
    def current_team(self) -> Optional[Team]:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)

    def push_team(self, team):
        method = "TeamStack.push_team"

        if team is None:
            raise PushingNullEntityException(f"{method}: {PushingNullEntityException.DEFAULT_MESSAGE}")

        if not isinstance(team, Team):
            raise TypeError(f"{method}: Expected a Team got {type(team).__name__}")

        if self._items is None:
            raise CorruptedStackException(f"{method}: {CorruptedStackException.DEFAULT_MESSAGE}")

        if self.current_team == team:
            raise DuplicatePushException(f"{method} {DuplicatePushException.DEFAULT_MESSAGE}")

        self._items.append(team)

