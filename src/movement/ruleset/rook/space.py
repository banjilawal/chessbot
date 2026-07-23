# src/space/ruleset/rook/space.py

"""
Module: space.ruleset.rook.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict


from model import Rook
from schema import Ruleset
from space import TraversalPattern, TraversalRuleset


class RookTraversalRuleset(TraversalRuleset[Rook]):
    """
    Role:
        -   Data Holder
        -   Immutability

    Responsibilities:
        1.  Determine potential destinations from RookToken's current position
        
    Attributes:
        ruleset: Dict[str: TraversalPattern]

    Provides:

    Super Class:
        TraversalRuleset
    """
    
    def __init__(self, ruleset: Dict[str: TraversalPattern] = Ruleset.ROOK.entries):
        """
        Args:
            ruleset: Dict[str: TraversalPattern] = Ruleset.ROOK.items
        """
        super().__init__(ruleset=ruleset)
    
