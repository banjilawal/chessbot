# src/logic/span/span.py

"""
Module: logic.span.span
Author: Banji Lawal
Created: 2026-02-26
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, List, TypeVar

from logic.span import Ray

T = TypeVar('T')

class Span(ABC, Generic[T]):
    """
    # ROLE: Data-Holder

    # RESPONSIBILITIES:
    1.  Stores rays projected from a common origin.

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   origin: T
        *   rays: List[T]

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   origin: T
        *   rays: List[Ray[T]]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
    None
    """
    _origin: T
    _rays: List[Ray[T]]
    
    def __init__(self, origin: T, rays: List[Ray[T]]):
        self._origin = origin
        self._rays = rays
        
    @property
    def length(self) -> int:
        return len(self._rays)
    
    @property
    def origin(self) -> T:
        return self._origin
    
    @property
    def rays(self) -> List[Ray[T]]:
        return self._rays
    
    @property
    def degrees(self) -> int:
        return len(self._rays)
    
    @property
    def is_empty(self) -> bool:
        return len(self._rays) == 0
        
    