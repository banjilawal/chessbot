# src/model/name/model.py

"""
Module: model.name.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import List

from system import MAX_NAME_LENGTH, MIN_NAME_LENGTH


class NamingRuleSet:
    _min_length: int
    _max_length: int
    
    def __init__(
            self,
            min_length: int = MIN_NAME_LENGTH,
            max_length: int = MAX_NAME_LENGTH,
    ):
        self._min_length = min_length
        self._max_length = max_length
        
    @property
    def min_length(self) -> int:
        return self._min_length
    
    @property
    def max_length(self) -> int:
        return self._max_length
    
    @property
    def to_list(self) -> List[int]:
        return [self._min_length, self._max_length]
    
    @property
    def to_dict(self) -> dict:
        return {
            "min_length": self._min_length,
            "max_length": self._max_length,
        }
