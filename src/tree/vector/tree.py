# src/tree/vector/tree.py

"""
Module: tree.vector.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List, cast

from container import VectorSet
from model import Vector
from tree import Tree


class VectorTree(Tree[Vector]):
    """
    Role:
        -   Data Holder
        -   Data protection

    Responsibilities:
        1.  Immutable unordered set of vectors.

    Attributes:
        items: Tuple[Vector, ...]

    Provides:

    Super Class:
        Tree
    """
    
    def __init__(self, root: Vector, branches: List[VectorSet]):
        """
        Args:
            items: Optional[Tuple[Vector, ...]]
        """
        super().__init__(root=root, branches=branches)
        
    @property
    def root(self) -> Vector:
        return cast(Vector, super().root)
    
    @property
    def branches(self) -> List[VectorSet]:
        return cast(List[VectorSet], super().branches)
        