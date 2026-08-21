# src/collection/tree/tree.py

"""
Module: collection.tree.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from collection import Chain
from domain import Model

T = TypeVar("T", bound="Model")

class Tree(ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        root: T
        branches: List[Chain]

    Provides:

    Super Class:
    """
    _root: T
    _branches: List[Chain]
    
    def __init__(self, root: T, branches: List[Chain]):
        """
        Args:
            root: T
            branches: List[Chain]
        """
        self._root = root
        self._branches = branches
        
    @property
    def root(self) -> T:
        return self._root
    
    @property
    def branches(self) -> List[Chain]:
        return self._branches
    
    
    @property
    def is_headless(self) -> bool:
        return self.root is None
    
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