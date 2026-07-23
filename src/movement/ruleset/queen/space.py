# src/space/ruleset/queen/space.py

"""
Module: space.ruleset.queen.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from model import Queen
from schema import Ruleset
from space import TraversalPattern, TraversalRuleset


class QueenTraversalRuleset(TraversalRuleset[Queen]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from QueenToken's current position

    Attributes:
        ruleset: Dict[str: TraversalPattern]

    Provides:

    Super Class:
        TraversalRuleset
    """
    
    def __init__(self, ruleset: Dict[str: TraversalPattern] = Ruleset.QUEEN.entries):
        """
        Args:
            ruleset: Dict[str: TraversalPattern] = Ruleset.ROOK.items
        """
        super().__init__(ruleset=ruleset)
    
