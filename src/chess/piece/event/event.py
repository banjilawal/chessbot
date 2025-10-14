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


class EntityOne:


from typing import Optional

from chess.square import Square
from chess.event import Event
from chess.piece import Piece, TravelContext

class TravelEvent(Event[Piece,Square]):
  """
  Details for executing an `OccupationTransaction`.

  Attributes:
    * `_actor` (`Piece`)
    * `_parent` (`Event`)
    * `_resource` (`Square`)
    * `_context` (`TravelContext`)
  """

  _actor: Piece
  _parent: Event
  _resource: Square
  _context: TravelContext

  def __init__(
      self,
      actor: Piece,
      destination_square: Square,
      context: TravelContext,
      parent: Optional[Event]=None
  ):
    """
    Constructor for TravelEvent

    Attributes:
      * `actor` (`Piece`):
      * `destination_square` (`Square`):
      * `parent` (`Event`):
      * `roster` (`TravelContext`):
    """
    super().__init__(actor=actor, resource=destination_square, parent=parent, context=context)

  @property
  def destination_square(self) -> Square:
    return self.resource

  def __eq__(self, other) -> bool:
    if super().__eq__(other):
      if isinstance(other, TravelEvent):
        return self._id == other.id
    return False