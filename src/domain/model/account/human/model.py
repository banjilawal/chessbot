# src/domain/model/account/human/model.py

"""
Module: domain.model.account.human.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Account


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
        firstname: str
        lastname: str
        email: str

     Provides:

     Super Class:
        Account
     """
    _firstname: str
    _lastname: str
    _email: str
    
    def __init__(
            self,
            id: int,
            firstname: str,
            lastname: str,
            email: str
    ):
        """
        Args:
            firstname: str
            lastname: str
            email: str
        """
        super().__init__(id=id)
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        
    @property
    def firstname(self) -> str:
        return self._firstname
    
    @property
    def lastname(self) -> str:
        return self._lastname
    
    @property
    def email(self) -> str:
        return self._email
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, HumanAccount):
            return self.id == other.id
        return False
