# src/chess/owner/travel/blocking/validator.py

"""
Module: `chess.owner.travel.blocking.event`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from typing import Optional

from chess.board import Board
from chess.system import Event
from chess.square import Square
from chess.piece import Piece, TravelEvent

class BlockingEvent(TravelEvent):
  _friend: Piece

  def __init__(
    self,
    id: int,
    actor: Piece,
    friend: Piece,
    blocked_square: Square,
    execution_environment: Board,
    parent: Optional[Event] = None
  ):
    super().__init__(
      id=id,
      actor=actor,
      parent=parent,
      destination_square=blocked_square,
      execution_environment = execution_environment
    )
    self._friend = friend


  @property
  def friend(self) -> Piece:
    return self._friend


  @property
  def blocked_square(self) -> Square:
    return self.destination_square


  def __eq__(self, other) -> bool:
    if super().__eq__(other):
      if isinstance(other, BlockingEvent):
        return True
    return False

  def __hash__(self) -> int:
    return hash(self.id)
