from typing import List

from chess.square import Square
from chess.piece.discover import Discovery
from chess.piece.piece import Piece


class ScoutReportAnalysis:
  _id: int
  _chess_piece: Piece
  _enemies: List[Piece]
  _vacant_squares: List[Square]
  _obstructions: List[Discovery]

  _obstruction_count: int
  _vacancy_count: int
  _enemy_count: int

  def __init__(self,
         analysis_id: int,
         chess_piece: Piece,
         enemies: List[Piece],
         vacant_squares: List[Square],
         obstructions: List[Discovery]
         ):
    self._id = analysis_id
    self._chess_piece = chess_piece
    self._enemies = enemies
    self._vacant_squares = vacant_squares
    self._obstructions = obstructions

    self._obstruction_count = len(self._obstructions)
    self._vacancy_count = len(self._vacant_squares)
    self._enemy_count = len(self._enemies)

  @property
  def id(self) -> int:
    return self._id

  @property
  def chess_piece(self) -> Piece:
    return self._chess_piece

  @property
  def enemies(self) -> List[Piece]:
    return self._enemies

  @property
  def vacant_squares(self) -> List[Square]:
    return self._vacant_squares

  @property
  def obstructions(self) -> List[Discovery]:
    return self._obstructions

  @property
  def obstruction_count(self) -> int:
    return self._obstruction_count

  @property
  def vacancy_count(self) -> int:
    return self._vacancy_count

  @property
  def enemy_count(self) -> int:
    return self._enemy_count

