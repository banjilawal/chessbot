"""
Module: owner
Author: Banji Lawal
Created: 2025-09-28
Purpose:
  Defines the Piece class hierarchy for the chess engine, including abstract and
  concrete pieces such as KingPiece and CombatantPiece. Pieces track identity, team
  membership, rank, and board_validator position, and manage interactions with other pieces.

Contents:
  - Piece: Abstract base class representing team chess owner with position and rank.
  - KingPiece: Concrete subclass representing team occupation owner.
  - CombatantPiece: Concrete subclass representing team owner capable of capturing others.
  - CoordStack, Checker, Discoveries: Supporting classes for tracking owner positions
   and discoveries.
  - Validators and exceptions related to owner creation and validate.

Notes:
  This module is part of the chess.owner package. Validation exceptions are defined
  in PieceValidator and related error classes. Piece objects are designed to be
  immutable in their core properties.
"""

from typing import Callable, Optional, cast

from chess.piece import Piece
from chess.rank import Rank
from chess.team import Team


class CombatantPiece(Piece):
  _captor: Optional[Piece]


  def __init__(self, id: int, name: str, rank: Rank, team: Team):
    super().__init__(id, name, rank, team)
    self._captor = None


  @property
  def captor(self) -> Optional[Piece]:
    return self._captor


  @captor.setter
  def captor(self, captor: Piece):
    self._captor = captor


  def __eq__(self, other):
    if super().__eq__(other):
      if isinstance(other, CombatantPiece):
        return True
    return False

  def __hash__(self):
    return hash(self._id)



