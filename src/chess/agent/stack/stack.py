# src/chess/agent/stack/stack

"""
Module: chess.agent.stack.stack
Author: Banji Lawal
Created: 2025-08-16
version: 1.0.0
"""


from typing import List, Optional

from chess.team import Team


class TeamStack:
  _size: int
  _teams: List[Team]
  _current_team: Team

  def __init__(self):
    self._teams = List[Team]
    self._current_team = self._teams[-1] if self._teams else None
    self._size = len(self._teams)

  @property
  def items(self) -> list[Team]:
    return self._teams
  
  @property
  def size(self) -> int:
    return len(self._teams)

  @property
  def current_team(self) -> Optional[Team]:
    return self._teams[-1] if self._teams else None

  def is_empty(self) -> bool:
    return len(self._teams) == 0



