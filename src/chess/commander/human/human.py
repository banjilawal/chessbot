from abc import ABC
from typing import Optional, cast, TYPE_CHECKING

from chess.coord import CoordValidator
from assurance import IdValidator, NameValidator
from chess.system import AutoId
from chess.team import Team
from chess.piece import Piece
from chess.commander import CommandHistory

if TYPE_CHECKING:
  pass

@AutoId
class Human(Commander):

  def __init__(self, name: str):
    super().__init__(name)

  def __eq__(self, other):
    if not super().__eq__(other):
      return False
    if isinstance(other, Human):
      return self.id == other.id
    return False