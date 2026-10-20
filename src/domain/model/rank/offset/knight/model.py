# src/domain/model/rank/knight/model.py

"""
Module: domain.model.rank.knight.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from __future__ import annotations

from typing import Optional

from domain import ElevatableRank, OffsetRank, Persona


class Knight(OffsetRank, ElevatableRank):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Maps to how a Token moves on the Board.
        2.  What Encounters a Token can engage.

    Attributes:
        persona: Persona.KNIGHT

    Provides:

    Super Class:
        OffsetRank
    """
    
    def __init__(self, persona: Optional[Persona] | None = None):
        """
        Args:
            persona: Optional[Persona]
        """
        super().__init__(persona=persona or Persona.KNIGHT)