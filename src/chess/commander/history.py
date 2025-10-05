from typing import Optional

from typing_extensions import TYPE_CHECKING
from chess.team import Team

from chess.exception.stack_exception import (
  PushingNullEntityException,
  CorruptedStackException,
  DuplicatePushException
)

# if TYPE_CHECKING:
#   pass


class CommandHistory:
  _teams: list[Team]
  _current_team: Team

  def __init__(self):
    self._teams = []
    self._current_team = self._teams[-1] if self._teams else None

  @property
  def items(self) -> list['Team']:
    """
    Returns a read-only view of the stack's contents. The returned sequence is safe to
    iterate and index, but mutating it will not affect the original stack.
    """

    return self._teams


  @property
  def current_team(self) -> Optional['Team']:
    return self._teams[-1] if self._teams else None


  def is_empty(self) -> bool:
    return len(self._teams) == 0


  def size(self) -> int:
    return len(self._teams)


  def find_by_id(self, id: int) -> Optional['Team']:
    for side in self._teams:
      if side.id == id:
        return side
    return None


  def add_team(self, team: Team):
    method = "CommandHistory.add_team"

    if team is None:
      raise PushingNullEntityException(f"{method}: {PushingNullEntityException.DEFAULT_MESSAGE}")

    if self._teams is None:
      raise CorruptedStackException(f"{method}: {CorruptedStackException.DEFAULT_MESSAGE}")

    if self.current_team == team:
      raise DuplicatePushException(f"{method} {DuplicatePushException.DEFAULT_MESSAGE}")

    self._teams.append(team)

