# src/toolkit/builder/register/identity/toolkit.py

"""
Module: toolkit.builder.register.identity.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import cast

from register import Register


class IdentityRegister(Register):
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
    """
    
    def __init__(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(a=id, b=name)
        
    @property
    def id(self) -> int:
        return cast(int, self.a)
    
    @property
    def name(self) -> str:
        return cast(str, self.name)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, IdentityRegister):
            return (
                    self.id == other.id and
                    self.name == other.name
            )
    
