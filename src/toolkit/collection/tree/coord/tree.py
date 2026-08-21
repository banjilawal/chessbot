# src/toolkit/collection/tree/coord/tree.py

"""
Module: toolkit.collection.tree.coord.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from collection import CoordSet
from domain.model import Coord
from tree import Tree


class CoordTree(Tree[Coord]):
    """
    Role:
        -   Data Holder
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of coords.

    Attributes:
        items: Tuple[Coord, ...]

    Provides:

    Super Class:
        Tree
    """
    
    def __init__(self, root: Coord, branches: List[CoordSet]):
        """
        Args:
            items: Optional[Tuple[Coord, ...]]
        """
        super().__init__(root=root, branches=branches)
        
    @property
    def root(self) -> Coord:
        return cast(Coord, super().root)
    
    @property
    def branches(self) -> List[CoordSet]:
        return cast(List[CoordSet], super().branches)

        