# src/collection/stack/model/account/collection.py

"""
Module: collection.stack.model.account.collection
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Iterator, List, Optional, cast

from artifcat import DeletionResult, InsertionResult, SearchResult
from collection import ModelStack
from domain import Account


class AccountStack(ModelStack[Account]):
    """
    Role:
        -   Collection

    Responsibilities:
        1.  Stack of unique Account objects.

    Attributes:
        items: List[Account]
 
    Provides:

    Super Class:
        ModelStack
    """
    
    def __init__(self, items: Optional[List[Account]] | None = None):
        super().__init__()
    
    @property
    def items(self) -> List[Account]:
        return cast(List[Account], super().items)
    
    @property
    @abstractmethod
    def push(self) -> InsertionResult:
        pass
    
    @property
    @abstractmethod
    def search(self) -> SearchResult[List[Account]]:
        pass
    
    @property
    @abstractmethod
    def pop(self) -> DeletionResult[Account]:
        pass
    
    @property
    def iterator(self) -> Iterator[Account]:
        return iter(self.items)
    
    