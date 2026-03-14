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

T = TypeVar("T")

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
    _sub_span_roots: List[T]
    
    def __init__(self, origin: T, rays: List[Ray[T]], sub_span_roots: List[T]):
        self._origin = origin
        self._rays = [Ray[T]]
        self._sub_span_roots = sub_span_roots
        
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
    def sub_span_roots(self) -> List[T]:
        return self._sub_span_roots
    
    @property
    def degrees(self) -> int:
        return len(self._rays)
    
    @property
    def is_empty(self) -> bool:
        return self.degrees == 0 and not self.has_sub_spans
    
    @property
    def number_of_sub_spans(self) -> int:
        return len(self._sub_span_roots)
    
    @property
    def has_sub_spans(self) -> bool:
        return len(self._sub_span_roots) > 0
        
    