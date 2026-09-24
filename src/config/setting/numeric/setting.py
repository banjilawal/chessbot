# src/config/setting/numeric/min_id/setting.py

"""
Module: config.setting.numeric.min_id.setting
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Mapping, Optional
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
    _value: NumericPropertyValue
    _entry: Mapping[NumericPropertyName, int]
    
    def __init__(
            self,
            value: Optional[NumericPropertyValue] | None = None,
    ):
        """
        Args:
            value: Optional[NumericPropertyValue]
        """

        self._vale = value or NumericPropertyValue()
        self._entry = Mapping[NumericPropertyName, int] = field(
            default_factory=lambda: MappingProxyType(
                {
                    NumericPropertyName.MIN_ID: self._value.min_id,
                    NumericPropertyName.FLOOR: self._value.floor,
                    NumericPropertyName.CEILING: self._value.ceiling,
                    NumericPropertyName.INFINITY: self._value.infinity,
                    NumericPropertyName.NEGATIVE_INFINITY: self._value.negative_infinity,
                }
            )
        )
        
    @property
    def entry(self) -> Mapping[NumericPropertyName, int]:
        return self._entry
    
    @property
    def min_id(self) -> int:
        return self._entry[NumericPropertyName.MIN_ID]
    
    @property
    def floor(self) -> int:
        return self._entry[NumericPropertyName.FLOOR]
    
    @property
    def ceiling(self) -> int:
        return self._entry[NumericPropertyName.CEILING]
    
    @property
    def infinity(self) -> int:
        return self._entry[NumericPropertyName.INFINITY]
    
    @property
    def negative_infinity(self) -> int:
        return self._entry[NumericPropertyName.NEGATIVE_INFINITY]