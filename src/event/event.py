# src/event.py

"""
Module: event.event
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional



class Event:
        _id: int
        _parent: Optional[Event]
        
        def __init__(self, id: int, parent: Optional[Event] | None = None):
                self._id = id
                self._parent = parent
                
        @property
        def id(self) -> int:
                return self._id
        
        @property
        def parent(self) -> Optional[Event]:
                return self._parent
        
        def __eq__(self, other: object) -> bool:
                if other is self: return True
                if other is None: return False
                if isinstance(other, Event):
                        return self._id == other.id
                return False
                