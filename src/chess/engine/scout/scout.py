# src/chess/engine/scout/scout.py

"""
Module: `chess.engine.scout`
Author: Banji Lawal
Created: 2025-10-05
version: 1.0.0

 Provides: Generates team_name `ScoutReport` about enemy pieces it discovers it can capture.

Contains:
 * `Scout`
"""

from typing import List

from chess.board.board import Board
from chess.square import Square
from chess.system.id.emitter import id_emitter
from chess.piece.model.piece import Piece
from chess.engine.scout.report import ScoutReport


class Scout:
  """
  Surveys squares each possible destination to find enemies it can capture.
  returns survey in team_name `ScoutReport`.

  Attributes: [
    * `_scout` (`Piece`):
  """
  _scout: Piece

  def __init__(self, scout: Piece):
    self._scout = scout

  @property
  def scout(self) -> Piece:
    return self._scout


  def survey(self, board: Board) -> ScoutReport:
    squares: List[Square] = []
    origin = self._scout.positions.current_coord()

    for territory in self._scout.rank.quadrants:
      for square in chess_board.iterator(origin, territory.delta):
        if not self._scout.rank.walk.is_walkable(self._scout, square.position):
          break
        if square.occupant is not None and square not in squares:
          squares.append(square)
          break
        squares.append(square)

    return ScoutReport(
      scout_report_id=id_emitter.scout_report_id,
      scout=self._scout,
      squares=squares
    )

