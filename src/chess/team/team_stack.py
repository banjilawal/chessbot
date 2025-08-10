from typing import Optional, List

from chess.common.chess_exception import ChessException
from chess.team.team import Team


class PopEmptyTeamStackException(ChessException):
    default_message = "Cannot pop from empty team stack"

class PushNullTeamException(ChessException):
    default_message = "Cannot push p null team on to te stack"

class TeamStack:
    _stack: List[Team]

    def __init__(self):
        self._stack = []

    @property
    def stack(self) -> List[Team]:
        return self._stack

    def is_empty(self) -> bool:
        return self.size() == 0 and self.current_team() is None


    def size(self) -> int:
        return len(self._stack)


    def current_team(self) -> Optional[Team]:
        return self._stack[-1] if self._stack else None


    def push_team(self, team):
        method_name = "TeamStack.push"

        if self.current_team() != team:
            self._stack.append(team)

    def undo_push(self):
        if self.size() == 0:
            raise PopEmptyTeamStackException("Cannot pop from empty team stack")

        self._stak.pop()