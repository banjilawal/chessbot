# src/model/query/model.py

"""
Module: model.query.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar


T = TypeVar("T")

class Query(ABC, Generic[T]):
    """
    Role:
        -   Stateless Data-Holder

    Responsibilities:
        1.  Platform primitive to build Query APIs

    Attributes:
        context: Context[T]

    Provides:

    Super Class:
    """
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
    
    
