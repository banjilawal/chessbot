# src/model/identity/model.py

"""
Module: model.identity.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from model import Model


class Identity(Model):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Contains the id and name for an identity.

    Attributes:
        id: int
        name: str
            
    Provides:

    Super Class:
        Model
    """
    
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
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Identity):
            return (
                    self.id == other.id and
                    self.name == other.name
            )
        return False
    
