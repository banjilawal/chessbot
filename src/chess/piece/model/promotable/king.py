# src/chess/piece/model/promotable/king.py

"""
Module: chess.piece.model.promotable.king
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from typing import List


from chess.rank import Rank
from chess.team import Team
from chess.piece import PromotablePiece


class KingPiece(PromotablePiece):
  _is_checked: bool
  _is_checkmated: bool


  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)
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
    if super().__eq__(other):
      if isinstance(other, KingPiece):
        return True
    return False

  def __hash__(self):
    return hash(self._id)