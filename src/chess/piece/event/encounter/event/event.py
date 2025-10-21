from typing import Optional

from chess.board import Board
from chess.square import Square
from chess.system import AutoId, Event
from chess.piece import Piece, TravelEvent

# IF TYPE_CHECKING:
#   from chess.piece.event.encounter.event import EncounterEvent


@AutoId
class EncounterEvent(TravelEvent):
  _subject: Piece

  def __init__(
    self,
    actor: Piece,
    subject: Piece,
    subject_square: Square,
    execution_environment: Board,
    parent: Optional[Event] = None
  ):
    super().__init__(
      actor=actor,
      parent=parent,
      destination_square=subject_square,
      execution_environment = execution_environment
    )
    self._subject = subject


  @property
  def subject(self) -> Piece:
    return self._subject


  @property
  def subject_square(self) -> Square:
    return self.destination_square


  def __eq__(self, other):
    if not super().__eq__(other):
      return False
    if isinstance(other, 'EncounterEvent'):
      return self.id == other.id
