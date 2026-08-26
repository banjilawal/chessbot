# src/collection/tree/vector/tree.py

"""
Module: collection.tree.vector.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, Optional, cast

from collection import Tree, VectorChain
from domain import Vector, VectorNode



class VectorTree(Tree[Vector]):
    """
    Role:
        -  Data Holder
        -  Data protection

    Responsibilities:
        1.  Immutable unordered set of vectors.

    Attributes:
        root: VectorNode
        branches: Optional[List[VectorChain]]

    Provides:

    Super Class:
        Tree
    """
    
    def __init__(self, root: Vector, branches: Optional[List[VectorChain]] | None = None):
        """
        Args:
            root: VectorNode
            branches: Optional[List[VectorChain]]
        """
        super().__init__(root=root, branches=branches or List[VectorChain])
        
    @property
    def root(self) -> VectorNode:
        return cast(VectorNode, super().root)
    
    @property
    def branches(self) -> List[VectorChain]:
        return cast(List[VectorChain], super().branches)
        
        
    
        