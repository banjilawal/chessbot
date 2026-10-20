# src/domain/model/rank/bishop/model.py

"""
Module: domain.model.rank.bishop.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from __future__ import annotations

from typing import Optional

from domain import Persona, TraversalRank


class Bishop(TraversalRank):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Maps to how a Token moves on the Board.
        2.  What Encounters a Token can engage.

    Attributes:
        persona: Persona.BISHOP

    Provides:

    Super Class:
        Model
    """
    
    def __init__(self, persona: Optional[Persona] | None = None):
        """
        Args:
            persona: Optional[Persona]
        """
        super().__init__(persona=persona or Persona.BISHOP)
        
        
        
        
        
    