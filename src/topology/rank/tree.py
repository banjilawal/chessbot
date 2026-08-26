# src/topology/rank/tree.py

"""
Module: topology.rank.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import  annotations

from abc import ABC
from typing import Generic, TypeVar

from tree import Tree, VectorTree

T = TypeVar("T")

class Topology(ABC, Generic[T]):
    """
    Role:
        -  Data Holder

    Responsibilities:
        1.  Positions a projected from a Rank's signature.

    Attributes:
         tree: VectorTree

    Provides:

    Super Class:
    """
    _tree: VectorTree
    
    def __init__(self, tree: VectorTree):
        self._tree = tree
        
    @property
    def tree(self) -> Tree:
        return  self._tree