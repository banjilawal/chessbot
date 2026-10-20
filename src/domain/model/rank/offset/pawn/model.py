# src/domain/model/rank/pawn/model.py

"""
Module: domain.model.rank.pawn.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from __future__ import annotations

from typing import Optional

from domain import OffsetRank, Persona


class Pawn(OffsetRank):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Maps to how a PawnToken moves on the Board.
        2.  What Encounters a Token can engage.

    Attributes:
        persona: Persona.PAWN

    Provides:

    Super Class:
        OffsetRank
    """
    
    def __init__(self, persona: Optional[Persona] | None = None):
        """
        Args:
            persona: Optional[Persona]
        """
        super().__init__(persona=persona or Persona.PAWN)