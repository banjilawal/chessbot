from typing import List

from chess import rank
from chess.piece.checker import Checker
from chess.piece.model.promotable import PromotablePiece
from chess.rank import Rank
from chess.team import Team


class KingPiece(PromotablePiece):
  _is_checked: bool
  _is_checkmated: bool
  _checkers: List[Checker] = []

  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)
    self._checkers = []
    self._is_checked = False
    self._is_checkmated = False


  @@property
  def checkers(self) -> List[Checker]:
      return self._checkers


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
    if super().__eq__(other):
      if isinstance(other, KingPiece):
        return True
    return False

  def __hash__(self):
    return hash(self._id)