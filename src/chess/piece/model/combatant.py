"""
Module: piece
Author: Banji Lawal
Created: 2025-09-28
Purpose:
  Defines the Piece class hierarchy for the chess engine, including abstract and
  concrete pieces such as KingPiece and CombatantPiece. Pieces track identity, team
  membership, rank, and board_validator position, and manage interactions with other pieces.

Contents:
  - Piece: Abstract base class representing team chess piece with position and rank.
  - KingPiece: Concrete subclass representing team king piece.
  - CombatantPiece: Concrete subclass representing team piece capable of capturing others.
  - CoordStack, Discovery, Discoveries: Supporting classes for tracking piece positions
   and discoveries.
  - Validators and exceptions related to piece creation and validate.

Notes:
  This module is part of the chess.piece package. Validation exceptions are defined
  in PieceValidator and related error classes. Piece objects are designed to be
  immutable in their core properties.
"""
from typing import Optional


class CombatantPiece(Piece):
  _captor: Optional[Piece]

  def __init__(self, name: str, rank: 'Rank', team: 'Team'):
    super().__init__(name, rank, team)
    self._captor = None


  @property
  def captor(self) -> Optional[Piece]:
    return self._captor


  @captor.setter
  def captor(self, captor: Piece):
    self._captor = captor


  def __eq__(self, other):
    if not super().__eq__(other):
      return False

    if isinstance(other, CombatantPiece):
      return self.id == other.id



