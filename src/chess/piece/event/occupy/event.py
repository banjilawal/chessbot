from typing import Optional

from chess.square import Square
from chess.system import TransactionResult, AutoId, Event
from chess.piece import Piece, TravelEvent, TravelContext


@AutoId
class OccupationEvent(TravelEvent):
  _actor_square: Square


  _actor: Piece
  _parent: Event
  _resource: Square
  _context: TravelContext

  @LoggingLevelRouter.monitor
  def __init__(
      self,
      actor: Piece,
      destination_square: Square,
      context: TravelContext,
      parent: Optional[Event]=None

  def __init__(
    self,
    actor: Piece,
    actor_square: Square,
    destination_square: Square,
    context: TravelContext,
    parent: Optional[Event]=None
  ):
    super().__init__(actor=actor, destination_squ=destination_square, parent=parent, context=context)
    self._actor_square = actor_square


  @property
  def actor_square(self) -> Square:
    return self._actor_square


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, OccupationEvent):
        return self._id == other.id
    return False