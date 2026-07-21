# src/space/ruleset/bishop/space.py

"""
Module: space.ruleset.bishop.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from schema import Ruleset
from space import TraversalPattern, TraversalRuleset


class BishopTraversalRuleset(TraversalRuleset):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1.  The second component of a BishopBasis. Necessary for computing a BishopToken's destination vectors.

    Attributes:

    Provides:

    Super Class:
        TraversalRuleset
    """
    
    def __init__(
            self,
            entries: Dict[str: TraversalPattern] = Ruleset.BISHOP.entries
    ):
        """
        Args:
            entries: Dict[str: TraversalPattern]
        """
        super().__init__(entries=entries)
    
