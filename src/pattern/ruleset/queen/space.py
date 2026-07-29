# src/pattern/ruleset/queen/pattern.py

"""
Module: pattern.ruleset.queen.pattern
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from model import Queen
from schema import Ruleset
from pattern import TraversalSignature, TraversalRuleset


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
    
    def __init__(self, ruleset: Dict[str: TraversalSignature] = Ruleset.QUEEN.entries):
        """
        Args:
            ruleset: Dict[str: TraversalPattern] = Ruleset.ROOK.items
        """
        super().__init__(ruleset=ruleset)
    
