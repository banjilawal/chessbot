# src/domain/model/rank/model.py

"""
Module: domain.model.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import ElevatableRank, Persona, Rank


class TraversalRank(Rank, ElevatableRank, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Maps to how a Token moves on the Board.
        2.  What Encounters a Token can engage.

    Attributes:
        persona: Persona

    Provides:

    Super Class:
        Model
    """
    
    def __init__(self,persona: Persona):
        """
        Args:
            persona: Persona
        """
        super().__init__(persona=persona)