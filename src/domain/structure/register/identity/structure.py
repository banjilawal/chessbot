# src/domain/structure/register/coord/structure.py

"""
Module: domain.structure.register.coord.register
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, List, cast



class IdentityRegister:
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Contains the endpoints of a journey.

    Attributes:
        id: Coord
        name: Coord
        id_same_as_name: bool
        id_differs_from_name: bool
            
    Provides:

    Super Class:
        Register
    """
    _id: int
    _name: str
    
    def __init__(self, id: int, name: str,):
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
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
        }
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, IdentityRegister):
            return (
                    self._id == other.id and
                    self._name == other.name
            )
    
