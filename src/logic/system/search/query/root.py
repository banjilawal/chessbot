# src/logic/system/search/query/root.py

"""
Module: logic.system.search.query.root
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from abc import ABC
from typing import Generic, TypeVar

from logic.system.search import Context

T = TypeVar("T")

class Query(ABC, Generic[T]):
    _context: Context[T]
    
    def __init__(self, context: Context[T]):
        """
        Args:
            context: Context[T]
        """
        self._context = context
        
    @property
    def context(self) -> Context[T]:
        return self._context
    
    
