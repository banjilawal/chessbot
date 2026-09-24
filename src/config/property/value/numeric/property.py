# src/config/property/value/numeric/property.py

"""
Module: config.property.value.numeric.property
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

import sys
from typing import Optional


class NumericPropertyValue:
    """
     Role:
        1.  Configuration
        2.  Metadata

     Responsibilities:
         1. Values of NumericProperty attribute.

     Attributes:
        min_id: int
        floor: int
        ceiling: int
        infinity: int
        neative_infinity: int
        
     Provides:

     Super Class:
     """
    CEILING = 4096
    INFINITY = sys.maxsize

    _min_id: int
    _floor: int
    _ceiling: int
    _infinity: int
    
    def __init__(
            self,
            min_id: Optional[int] | None = None,
            floor: Optional[int] | None = None,
            ceiling: Optional[int] | None = None,
            infinity: Optional[int] | None = None,
    ):
        """
        Args:
            min_id: Optional[int]
            floor: Optional[int]
            ceiling: Optional[int]
            infinity: Optional[int]
        """
        self._min_id = min_id or 0
        self._floor = floor or 0
        self._ceiling = ceiling or self.CEILING
        self._infinity = infinity or self.INFINITY
        
    @property
    def min_id(self) -> int:
        return self._min_id
    
    @property
    def floor(self) -> int:
        return self._floor
    
    @property
    def ceiling(self) -> int:
        return self._ceiling
    
    @property
    def infinity(self) -> int:
        return self._infinity
    
    @property
    def negative_infinity(self) -> int:
        return  1 - self._infinity
    
        
        