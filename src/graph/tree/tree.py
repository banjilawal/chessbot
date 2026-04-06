# src/logic/pair/tree.py

"""
Module: logic.pair.tree
Author: Banji Lawal
Created: 2026-03-12
version: 1.0.0
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List

from model.graph.node import Node
from graph.pair import PairList
from graph.pair.listing.service import PairListService


@dataclass
class NodeTree:
    """
    # RESPONSIBILITY:
    1.  Represents the Pairs emanating from a source. The tree might have one
        root or subtrees.
    2.  It does not contain any link information
    """
    root: Node
    branches: List[PairList]
    branch_service: PairListService
    
    @property
    def degree(self) -> int:
        return len(self.branches)
    
    @property
    def is_empty(self) -> bool:
        return self.degree == 0