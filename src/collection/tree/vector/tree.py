# src/collection/tree/vector/tree.py

"""
Module: collection.tree.vector.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import List, cast

from collection import CoordSet, VectorSet
from domain.model import Coord, Vector
from tree import CoordTree, Tree


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
    
    @property
    def to_coord_tree(self) -> CoordTree:
        coord_branches = []
        for branch in self.branches:
            coord_branches.append(CoordSet(branch.to_coord_tuple()))
        origin = Coord(column=self._root.x, row=self._root.y)
        return CoordTree(root=origin, branches=coord_branches)
        
        
    
        