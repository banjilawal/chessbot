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

    Responsibilities:
        1.  The second component of a RookBasis. Necessary for computing a RookToken's destination vectors.

    Attributes:

    Provides:

    Super Class:
        TraversalRuleset
    """
    
    def __init__(
            self, entries: Dict[str: TraversalPattern] = Ruleset.ROOK.entries
    ):
        """
        Args:
            entries: Dict[str: TraversalPattern] = Ruleset.ROOK.entries
        """
        super().__init__(entries=entries)
    
