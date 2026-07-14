# src/space/axis/terminus/hash/space/axis/space.axis.terminus.py

"""
Module: space.axis.terminus.hash.terminus
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Dict

from space.bounds import AxisBounds
from space.axis.terminus import AxisTerminusEntry, terminusBound
from model import Vector


class AxisBoundsComputer:
    terminus_entry: AxisTerminusEntry = AxisTerminusEntry()
    
    _hash: Dict[str: terminusBound]
    
    def __init__(self, origin: Vector):
        self._terminus_entry = AxisTerminusEntry()
        
        self._hash = {
            "north": terminusBound(
                terminus=self._terminus_entry.north,
                bounds=AxisBounds.north(origin=origin)
            ),
            "east": terminusBound(
                terminus=self._terminus_entry.east,
                bounds=AxisBounds.east(origin=origin)
            ),
            "south": terminusBound(
                terminus=self._terminus_entry.south,
                bounds=AxisBounds.south(origin=origin),
            ),
            "west": terminusBound(
                terminus=self._terminus_entry.west,
                bounds=AxisBounds.west(origin=origin),
            ),
        }
        
    @property
    def north(self) -> terminusBound:
        return self._hash["north"]
    
    @property
    def east(self) -> terminusBound:
        return self._hash["east"]
    
    @property
    def south(self) -> terminusBound:
        return self._hash["south"]
    
    @property
    def west(self) -> terminusBound:
        return self._hash["west"]