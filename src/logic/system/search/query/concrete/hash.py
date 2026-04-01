# src/logic/system/collection/hash/lookup/exception.py

"""
Module: logic.system.collection.hash.lookup.lookup
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations

from enum import Enum
from typing import Generic, List, TypeVar

from logic.system import SearchRouter, Context, LoggingLevelRouter, SearchResult, Validator

E = TypeVar("E", bound=Enum)

class HashQuery(Query, Generic[E]):
    _hash: E
    
    def __init__(self, hash: E, super_key: Context[E]):
        """
        Args:
            hash: E
            super_key: Context[E]
        """
        super().__init__(context=super_key)
        self._hash = hash
    
    @property
    def hash(self) -> E:
        return self._hash
