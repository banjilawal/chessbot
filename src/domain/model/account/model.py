# src/domain/model/account/model.py

"""
Module: domain.model.account.model
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from abc import ABC

from domain import StateModel


class Account(StateModel, ABC):
    """
     Role:
         - Data Holder

     Responsibilities:
        2.  Direct a Team's pieces that are in an Arena's Board during a Game.

     Attributes:
         id: int

     Provides:

     Super Class:
        Model
     """
    
    def __init__(self, id: int):
        """
        Args:
            id: int
        """
        super().__init__(id=id)
    

    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Account):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
