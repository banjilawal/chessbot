# src/chess/piece/travel/event.py

"""
Module: `chess.piece.travel.travel`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Provides:
Concrete subclass of `Event`.

Contains:
 * `TravelEvent`
"""


from typing import Optional, cast

from chess.piece import Piece
from chess.board import Board
from chess.square import Square
from chess.system import Event, LoggingLevelRouter



class TravelEvent(Event[Piece, Square, Board]):

  @LoggingLevelRouter.monitor
  def __init__(
      self,
      id: int,
      actor: Piece,
      destination_square: Square,
      execution_environment: Board,
      parent: Optional[Event]=None
  ):
    super().__init__(
      id=id,
      actor=actor,
      parent=parent,
      resource=destination_square,
      execution_environment=execution_environment,
    )

  @property
  def destination_square(self) -> Square:
    return cast(Square, self._resource)

  def __eq__(self, other) -> bool:
    if super().__eq__(other):
      if isinstance(other, TravelEvent):
        return True
    return False

  def __hash__(self) -> int:
    return hash(self.id)