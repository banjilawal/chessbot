# src/space/hashtable/axis/space.py

"""
Module: space.hashtable.axis.space
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from mapping import AxisMapFunction, EastAxisMapFunction
from model import Vector
from recurrence import RecurrenceHashSet
from space import (
    Axis, AxisHashSet, EastAxis, NorthAxis, SouthAxis, WestAxis
)

class AxisRecurrenceHashSet(RecurrenceHashSet[Axis]):
    _expected_size: int
    _axis_hash_set: AxisHashSet
    
    def __init__(self, origin: Vector,):
        super().__init__(origin=origin)
        
        self._axis_hash_set = AxisHashSet(self.origin)
        east_axis = EastAxis(self.)
        self._hash_table = {
            "east_axis": {EastEastAxis(self.origin): EastAxisMapFunction(),
            "north_axis": NorthAxis(self.origin),
            "south_axis": SouthAxis(self.origin),
            "west_axis": WestAxis(self.origin),
        }
        self._expected_size = len(self._hash_table)
        
        
    @property
    def hash_table(self) -> Dict[str, Axis]:
        return self._hash_table

    @property
    def size(self) -> int:
        return len(self._hash_table)
    
    @property
    def expected_size(self) -> int:
        return self._expected_size
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_expected_size(self) -> bool:
        return self.size == self._expected_size
    
    @property
    def is_wrong_size(self) -> bool:
        return not self.is_expected_size
    
    @property
    def is_axis_hash_set(self) -> bool:
        for key in self._hash_table.keys():
            if not isinstance(self._hash_table[key], Axis):
                return False
        return True
    
    @property
    def is_not_axis_hash_set(self) -> bool:
        return not self.is_axis_hash_set
    

