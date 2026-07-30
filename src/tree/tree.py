# src/tree/tree.py

"""
Module: tree.tree
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Container, Generic, List, TypeVar


T = TypeVar("T")

class Tree(ABC, Generic[T]):
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
    _branches: List[Container[T]]
    
    def __init__(self, root: T, branches: [Container[T]]):
        self._root = root
        self._branches = branches
        
    @property
    def root(self) -> T:
        return self._root
    
    @property
    def branches(self) -> List[Container[T]]:
        return self._branches
    
    
    @property
    def number_of_branches(self) -> int:
        return len(self._branches)
    

    
    @property
    def has_no_branches(self) -> bool:
        return self.number_of_branches == 0