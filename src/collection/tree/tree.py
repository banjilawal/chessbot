# src/collection/tree/tree.py

"""
Module: collection.tree.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, Optional, TypeVar

from collection import Chain
from domain import Node

T = TypeVar("T", bound="Node")

class Tree(ABC, Generic[T]):
    """
    Role:
        - Data Holder
        - Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        root: T
        branches: List[Chain[T]]

    Provides:

    Super Class:
    """
    _root: T
    _branches: List[Chain[T]]
    
    def __init__(self, root: T, branches: Optional[List[Chain[T]]] | None = None):
        """
        Args:
            root: T
            branches: Optional[List[Chain[T]]]
        """
        self._root = root
        self._branches = branches or []
        
    @property
    def root(self) -> T:
        return self._root
    
    @property
    def branches(self) -> List[Chain[T]]:
        return self._branches
    
    
    @property
    def is_headless(self) -> bool:
        return self.root.is_empty
    
    @property
    def is_not_headless(self) -> bool:
        return not self.is_headless
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def size(self) -> int:
        if self.is_headless:
            return self.number_of_branches
        return self.number_of_branches + 1

    @property
    def number_of_branches(self) -> int:
        return len(self._branches)
    
    @property
    def has_no_branches(self) -> bool:
        return self.number_of_branches == 0