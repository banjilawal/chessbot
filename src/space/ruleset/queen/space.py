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

    Responsibilities:
        1.  The second component of a QueenBasis. Necessary for computing a QueenToken's destination vectors.

    Attributes:

    Provides:

    Super Class:
        TraversalRuleset
    """
    
    def __init__(
            self,
            entries: Dict[str: TraversalPattern] = Ruleset.QUEEN.entries
    ):
        """
        Args:
            entries: Dict[str: TraversalPattern]
        """
        super().__init__(entries=entries)
    
