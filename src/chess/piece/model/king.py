from typing import Callable, cast

from chess.rank import Rank
from chess.team import Team
from chess.piece import Piece

InitMethod = Callable[[str, Rank, Team], None]

class KingPiece(Piece):
  _id: int
  _is_checked: bool
  _is_checkmated: bool

  def __init__(self, name: str, rank: Rank, team: Team):
    init_call = cast(InitMethod, super().__init__)
    init_call(name, rank, team)

    self._is_checked = False
    self._is_checkmated = False


  @property
  def is_checked(self) -> bool:
    return self._is_checked

  @property
  def is_checkmated(self) -> bool:
    return self._is_checkmated

  @is_checked.setter
  def is_checked(self, is_checked: bool):
    self._is_checked = is_checked

  @is_checkmated.setter
  def is_checkmated(self, is_checkmated: bool):
    if self._is_checked:
      self._is_checkmated = is_checkmated
    else:
      raise Exception("Cannot set checkmated status if not checked")


  def __eq__(self, other):
    if not super().__eq__(other):
      return False
    if isinstance(other, KingPiece):
      return True
    return False

  def __hash__(self):
    return hash(self._id)