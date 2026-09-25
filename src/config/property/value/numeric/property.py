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

    _min_id: int = 0
    _floor: int = 0
    _ceiling: int = 4096
    _infinity: int = sys.maxsize
    
    # def __init__(
    #         cls,
    #         min_id: Optional[int] | None = None,
    #         floor: Optional[int] | None = None,
    #         ceiling: Optional[int] | None = None,
    #         infinity: Optional[int] | None = None,
    # ):
    #     """
    #     Args:
    #         min_id: Optional[int]
    #         floor: Optional[int]
    #         ceiling: Optional[int]
    #         infinity: Optional[int]
    #     """
    #     cls._min_id = min_id or 0
    #     cls._floor = floor or 0
    #     cls._ceiling = ceiling or cls._CEILING
    #     cls._infinity = infinity or cls._INFINITY
        
    @classmethod
    def min_id(cls) -> int:
        return cls._min_id
    
    @classmethod
    def floor(cls) -> int:
        return cls._floor
    
    @classmethod
    def ceiling(cls) -> int:
        return cls._ceiling
    
    @classmethod
    def infinity(cls) -> int:
        return cls._infinity
    
    @classmethod
    def negative_infinity(cls) -> int:
        return  1 - cls._infinity
    
        
        