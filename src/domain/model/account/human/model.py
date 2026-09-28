# src/domain/model/searchable/state/account/human/model.py

"""
Module: domain.model.searchable.state.account.human.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import Account
from game import GameAdviser


class HumanAccount(Account):
    """
     Role:
         - Data Holder

     Responsibilities:
        1.  Create, play, save, or terminate a Game.
        2.  Direct a Team's pieces that are in an Arena's Board.
        3.  Can seek advice on moves.
        4.  Can look up their previous games.

     Attributes:
         id: int
         name: str
         adviser: Optional[GameAdviser]

     Provides:

     Super Class:
        Account
     """
    
    def account(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str
        """
        super().__init__(id=id, name=name)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, HumanAccount):
            return self.id == other.id
        return False
