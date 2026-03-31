# src/transport/adt/message/address.py

"""
Module: transport.adt.message.address
Author: Banji Lawal
Created: 2026-03-30
version: 1.0.0
"""

from __future__ import annotations

class AddressTag:
    _id: int
    _name: str
    
    def __init__(self, id: int, name: str):
        """
        Args:
            id: int
            name: str
        """
        self._id = id
        self._name = name
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AddressTag):
            return self._id == other.id and self._name.upper() == other.name.upper()
        return False