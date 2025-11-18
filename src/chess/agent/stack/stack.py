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
  _teams: List[Team]
  _current_team: Team

  def __init__(self):
    self._teams = List[Team]
    self._current_team = self._teams[-1] if self._teams else None

  @property
  def items(self) -> list[Team]:
    return self._teams


  @property
  def current_team(self) -> Optional[Team]:
    return self._teams[-1] if self._teams else None


  def is_empty(self) -> bool:
    return len(self._teams) == 0


  def size(self) -> int:
    return len(self._teams)

  
  # src/chess/agent/stack/stack
  
  """
  Module: chess.agent.stack.stack
  Author: Banji Lawal
  Created: 2025-09-16
  version: 1.0.0
  """
  
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
        raise NullItemException(f"{method_name}: {NullItemException.DEFAULT_MESSAGE}")
      
      if self._items is None:
        raise CorruptedStackException(f"{method_name}: {CorruptedStackException.DEFAULT_MESSAGE}")
      
      if self.current_coord == coord:
        raise DuplicatePushException(f"{method_name}: {DuplicatePushException.DEFAULT_MESSAGE}")
      self._items.append(coord)
    
    def undo_push(self):
      method_name = "CoordStack.undo_push"
      
      if len(self._items) == 0:
        raise PopEmptyStackException(f"{method_name}: {PopEmptyStackException.DEFAULT_MESSAGE}")
      self._items.pop()
  #
  #
  # def main():
  #   stack = CoordStack()
  #   stack.push_coord(Coord(1, 1))
  #   stack.push_coord(Coord(1, 1))
  #   print(f"Current Coord: {stack.current_coord}")
  #   stack.undo_push()
  #   print(f"Current Coord after undo: {stack.current_coord}")
  #
  #
  # if __name__ == '__main__':
  #   main()

