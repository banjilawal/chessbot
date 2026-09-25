# src/config/setting/numeric/min_id/setting.py

"""
Module: config.setting.numeric.min_id.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Mapping, Optional
from types import MappingProxyType
from dataclasses import field

from config import NumericPropertyName, NumericPropertyValue


class NumericSetting:
    """
    Role
        - Property Settings
  
    Responsibilities:
        1.  Default Numeric properties.
  
    Attributes:
        min_id: int
        floor: int
        ceiling: int
        infinity: int
        neative_infinity: int
  
    Provides:
  
    Super Class:
    """
    _entry: Dict[NumericPropertyName, int] = {
        NumericPropertyName.MIN_ID: NumericPropertyValue.min_id(),
        NumericPropertyName.FLOOR: NumericPropertyValue.floor(),
        NumericPropertyName.CEILING: NumericPropertyValue.ceiling(),
        NumericPropertyName.INFINITY: NumericPropertyValue.infinity(),
        NumericPropertyName.NEGATIVE_INFINITY: NumericPropertyValue.negative_infinity(),
    }
    
    # def __init__(
    #         cls,
    #         value: Optional[NumericPropertyValue] | None = None,
    # ):
    #     """
    #     Args:
    #         value: Optional[NumericPropertyValue]
    #     """
    # 
    #     cls._vale = value or NumericPropertyValue()
    #     cls._entry = Mapping[NumericPropertyName, int] = field(
    #         default_factory=lambda: MappingProxyType(
    #             {
    #                 NumericPropertyName.MIN_ID: cls._value.min_id,
    #                 NumericPropertyName.FLOOR: cls._value.floor,
    #                 NumericPropertyName.CEILING: cls._value.ceiling,
    #                 NumericPropertyName.INFINITY: cls._value.infinity,
    #                 NumericPropertyName.NEGATIVE_INFINITY: cls._value.negative_infinity,
    #             }
    #         )
    #     )
    #     
    # @classmethod
    # def entry(cls) -> Mapping[NumericPropertyName, int]:
    #     return cls._entry
    
    @classmethod
    def min_id(cls) -> int:
        return cls._entry[NumericPropertyName.MIN_ID]
    
    @classmethod
    def floor(cls) -> int:
        return cls._entry[NumericPropertyName.FLOOR]
    
    @classmethod
    def ceiling(cls) -> int:
        return cls._entry[NumericPropertyName.CEILING]
    
    @classmethod
    def infinity(cls) -> int:
        return cls._entry[NumericPropertyName.INFINITY]
    
    @classmethod
    def negative_infinity(cls) -> int:
        return cls._entry[NumericPropertyName.NEGATIVE_INFINITY]