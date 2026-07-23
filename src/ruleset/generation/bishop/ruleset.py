# src/ruleset/generation/bishop/ruleset.py

"""
Module: ruleset.generation.bishop.ruleset
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from typing import List, Tuple

from model import Bishop
from ruleset import (
    NortheastQuadrantVectorSpec, NorthwestQuadrantVectorSpec, PatternGenerationRuleset, SequenceSpec,
    SoutheastQuadrantVectorSpec,
    SouthwestQuadrantVectorSpec
)


class BishopPatternRuleset(PatternGenerationRuleset[Bishop]):
    
    def __init__(self,
            ruleset=None
    ):
        super().__init__(ruleset=ruleset)
        if ruleset is None:
            ruleset = [
                NortheastQuadrantVectorSpec(),
                NorthwestQuadrantVectorSpec(),
                SoutheastQuadrantVectorSpec(),
                SouthwestQuadrantVectorSpec(),
            ]