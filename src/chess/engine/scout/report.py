from typing import List

from chess.square import Square
from chess.piece.model.piece import Piece


class ScoutReport:
  _id: int
  _scout: Piece
  _squares: List[Square]

  def __init__(self, scout_report_id: int, scout: Piece, squares: List[Square]):
    self._scout = scout
    self._squares = squares
    self._id = scout_report_id

  @property
  def id(self) -> int:
    return self._id

  @property
  def scout(self) -> Piece:
    return self._scout

  @property
  def squares(self) -> List[Square]:
    return self._squares


  def __eq__(self, other) -> bool:
    if other is self: return True
    if other is None: return False
    if not isinstance(other, ScoutReport): return False
    return self._id == other.id


  def __hash__(self) -> int:
    return hash(self._id)


  def __str__(self) -> str:
    return (
      f"ScoutReport(id:{self._id} scout:{self._scout.name} "
      f"observation_count:{len(self._squares)}"
    )