# chess/board/board.py

"""
Module: `chess.board.board`
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

Provides:
<SENTENCE_OR_PARAGRAPH_ABOUT_WHAT_THINGS_MODULE_PROVIDE>

Contains:
 * `EntityOne`
"""
from lib2to3.fixes.fix_input import context


class EntityOne:


from typing import Optional

from chess.square import Square
from chess.event import Event
from chess.piece import Piece, OccupationContext

class OccupationEvent(Event[Piece,Square]):
  """
  <WHAT_CLASS_DOES>.

  Attributes: [
    <No attributes. Implementors declare their own.>
  OR
    * `_attribute` (`data_type`): <sentence_if_necessary>
  ]
  """
  _actor: Piece
  _parent: Event
  _resource: Square
  _context: OccupationContext

  def __init__(self, actor: Piece, destination_square: Square, parent: Optional[Event]=None):
    """
    Constructor for OccupationEvent

    Attributes:
      * `actor` (`Piece`):
      * `destination_square` (`Square`):
      * `parent` (`Event`):
      * `context` (`OccupationContext`):
    """
    super().__init__(actor=actor, resource=destination_square, parent=parent, context=context)
    _actor = actor
    _parent = parent
    _resource = destination_square

  @property
  def destination_square(self) -> Square:
    return self.resource



  def __eq__(self, other) -> bool:
    if super().__eq__(other):
      if isinstance(other, OccupationEvent):
        return self._id == other.id
    return False