# src/collection/tree/tree.py

"""
Module: collection.tree.tree
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Collection, Generic, List, TypeVar


T = TypeVar("T")

class Tree(Collection, ABC, Generic[T]):
    """
    Role:
        -   Data Holder
        -   Data protection
        
    Responsibilities:
        1.  Immutable unordered set of items.

    Attributes:
        items: Tuple[T, ...]

    Provides:

    Super Class:
    """
    _root: T
    _branches: List[Collection[T]]
    
    def __init__(self, root: T, branches: [Collection[T]]):
        self._root = root
        self._branches = branches
        
    @property
    def root(self) -> T:
        return self._root
    
    @property
    def branches(self) -> List[Collection[T]]:
        return self._branches
    

    @property
    def number_of_branches(self) -> int:
        return len(self._branches)
    
    
    @property
    def has_no_branches(self) -> bool:
        return self.number_of_branches == 0