# src/chess/event/context.py

"""
Module: `chess.event.context`
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0

Provides:
Data dependencies an `actor` and `resource` need to execute a
`Transaction`.

Contains:
 * `ExecutionContext`
"""


from abc import ABC
from chess.system import Context


class ExecutionContext(ABC, Context):
  """
  Abstract Data Type of execution dependencies an `Event` passes to
  a `Transaction`.

  Attributes:
    No attributes. Subclasses declare their own.

  Attributes:
    `_actor (Piece):
    `_enemy (Piece):
    `_arena (Arena):
    `_board (Optional[Board):
    `_teams (Optional[List[Team):
    `_commanders ([List[Commander]):
  """


  # # Usage:
  # context = ExecutionContext(board=current_board, teams=all_teams)
  # outcome = executor.execute_directive(directive, context.to_dict())




  # def __init__(
  #   self,
  #   actor: Optional[Piece]=None,
  #   enemy: Optional[Piece]=None,
  #   arena: Optional[Arena]=None,
  #   board: Optional[Board]=None,
  #   teams: Optional[List[Team]]=None,
  #   commanders: Optional[List[Commander]]=None
  # ): #, game_state: GameState = None):
  #   if actor is not None and enemy is not None actor == enemy:
  #   self._actor = actor
  #   self._enemy = enemy
  #   self._arena = arena
  #   self._board = board
  #   self._teams = teams
  #   self._commanders = commanders
  #   # self.game_state = game_state
  #   self.turn = None
  #   # ... other context fields
  #
  #
  # @property
  # def actor(self) -> Optional[Piece]:
  #   return self._actor
  #
  # @property
  # def enemy(self) -> Optional[Piece]:
  #   return self._enemy
  #
  # @property
  # def arena(self) -> Optional[Arena]:
  #   return self._arena
  #
  # @property
  # def board(self) -> Optional[Board]:
  #   return self._board
  #
  # @property
  # def teams(self) -> Optional[List[Team]]:
  #   return self._teams
  #
  # @property
  # def commanders(self) -> Optional[List[Commander]]:
  #   return self._commanders
  #
  # def to_dict(self) -> dict:
  #   """Convert to dictionary for backward compatibility"""
  #   return {
  #     'arena': self._arena,
  #     'board': self._board,
  #     'teams': self._teams,
  #     'commanders': self._commanders,
  #     # 'game_state': self.game_state,
  #     'turn': self.turn
  #   }

#

