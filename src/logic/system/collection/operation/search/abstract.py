# src/logic/system/collection/operation/search/abstract.py

"""
Module: logic.system.collection.operation.search.abstract
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

from logic.system import SearchResult

T = TypeVar("T")


class SearchRouter(ABC, Generic[T]):
    
    @classmethod
    @abstractmethod
    def route(cls, *args, **kwargs) -> SearchResult[List[T]]:
        pass