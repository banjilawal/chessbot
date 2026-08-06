# src/topology/topology.py

"""
Module: topology.topology
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Container, Generic, TypeVar

from collection import VectorTree

T = TypeVar("T", bound="Rank")

class Topology(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        tree: VectorTree

    Provides:

    Super Class:
    """
    _tree: VectorTree
    
    def __init__(self, tree: VectorTree):
        """
        Args:
            tree: VectorTree
        """
        self._tree = tree
        
    @property
    def tree(self) -> VectorTree:
        return self._tree
    