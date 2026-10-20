# src/domain/model/rank/model.py

"""
Module: domain.model.rank.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC

from domain import Rank


class OffsetRank(Rank, ABC):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  Maps to how a new Token's next position is offset from its old position when it can move.

    Attributes:
        persona: Persona

    Provides:

    Super Class:
        Rank
    """
    
    def __init__(self, persona):
        """
        Args:
            persona: Persona
        """
        super().__init__(persona=persona)