# src/chess/piece/event/context.py

"""
Module: `chess.piece.event.context`
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0

Provides:
Data dependencies a `piece` and its `resource` need to execute a
`Transaction`.

Contains:
 * `OccupationContext`
"""

from typing import Optional

from chess.board import Board
from chess.piece import Piece
from chess.event import ExecutionContext


class OccupationContext(ExecutionContext):
  """
  Additional dependencies an `OccupationEvent` passes to an `OccupationTransaction`

  Attributes:
    `_board (`Board)`:
    `_destination_occupant (`Board`):
  """

  _board: Optional[Board]
  _destination_occupant: Optional[Piece]

  # # Usage:
  # context = ExecutionContext(board=current_board, teams=all_teams)
  # outcome = executor.execute_directive(directive, context.to_dict())

  def __init__(self, destination_occupant: Optional[Piece]=None, board: Optional[Board]=None):
    super().__init__()
    self._board = board
    self._destination_occupant = destination_occupant

  @property
  def board(self) -> Optional[Board]:
    return self._board

  @property
  def destination_occupant(self) -> Optional[Piece]:
    return self._destination_occupant
