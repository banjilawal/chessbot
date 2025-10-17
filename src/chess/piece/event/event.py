# src/chess/piece/event/event.py

"""
Module: `chess.piece.event.event`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Provides:
Concrete subclass of `Event`.

Contains:
 * `TravelEvent`
"""


from typing import Optional

from chess.board import Board
from chess.square import Square
from chess.piece import Piece, TravelContext
from chess.system import Event, AutoId, LoggingLevelRouter



class TravelEvent(Event[Piece,Square, Board]):

  @LoggingLevelRouter.monitor
  def __init__(
      self,
      actor: Piece,
      destination_square: Square,
      execution_environment: Board,
      parent: Optional[Event]=None
  ):
    super().__init__(
      actor=actor,
      resource=destination_square,
      parent=parent,
      execution_environment=execution_environment
    )


  @property
  def destination_square(self) -> Square:
    return self.resource


  def __eq__(self, other) -> bool:
    if not super().__eq__(other):
      return False
    if isinstance(other, TravelEvent):
        return self.id == other.id
    return False