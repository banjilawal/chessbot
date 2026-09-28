# src/domain/model/searchable/state/account/machine/model.py

"""
Module: domain.model.searchable.state.account.machine.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Account
from game import GameAdviser


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
    
    def __init__(self, id: int, name: str):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, MachineAccount):
            return self.id == other.id
        return False
