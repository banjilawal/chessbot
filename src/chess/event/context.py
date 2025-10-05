from abc import ABC
from typing import List, Optional

from chess.team import Team
from chess.board import Board
from chess.piece import Piece
from chess.arena.arena import Arena
from chess.commander import Commander

from chess.system import Context


class ExecutionContext(Context):
  """Container for execution dependencies"""

  # # Usage:
  # context = ExecutionContext(board=current_board, teams=all_teams)
  # outcome = executor.execute_directive(directive, context.to_dict())

  _actor: Optional[Piece]
  _enemy: Optional[Piece]
  _arena: Optional[Arena]
  _board: Optional[Board]
  _teams: Optional[List[Team]]
  _commanders: Optional[List[Commander]]


  def __init__(
    self,
    actor: Optional[Piece]=None,
    enemy: Optional[Piece]=None,
    arena: Optional[Arena]=None,
    board: Optional[Board]=None,
    teams: Optional[List[Team]]=None,
    commanders: Optional[List[Commander]]=None
  ): #, game_state: GameState = None):

    self._actor = actor
    self._enemy = enemy
    self._arena = arena
    self._board = board
    self._teams = teams
    self._commanders = commanders
    # self.game_state = game_state
    self.turn = None
    # ... other context fields


  @property
  def actor(self) -> Optional[Piece]:
    return self._actor

  @property
  def enemy(self) -> Optional[Piece]:
    return self._enemy

  @property
  def arena(self) -> Optional[Arena]:
    return self._arena

  @property
  def board(self) -> Optional[Board]:
    return self._board

  @property
  def teams(self) -> Optional[List[Team]]:
    return self._teams

  @property
  def commanders(self) -> Optional[List[Commander]]:
    return self._commanders

  def to_dict(self) -> dict:
    """Convert to dictionary for backward compatibility"""
    return {
      'arena': self._arena,
      'board': self._board,
      'teams': self._teams,
      'commanders': self._commanders,
      # 'game_state': self.game_state,
      'turn': self.turn
    }

#

