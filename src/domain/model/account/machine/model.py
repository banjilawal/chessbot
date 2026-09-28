# src/domain/model/account/machine/model.py

"""
Module: domain.model.account.machine.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Account


class MachineAccount(Account):
    """
     Role:
         - Data Holder

     Responsibilities:
        1.  Machine account can only execute GameAdviser recommendations about moves.

     Attributes:
         id: int
         name: str

     Provides:

     Super Class:
        Account
     """
    _name: str
    
    def __init__(self, id: int, name: str):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id)
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, MachineAccount):
            return self.id == other.id
        return False
