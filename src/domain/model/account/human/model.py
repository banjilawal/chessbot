# src/domain/model/account/human/model.py

"""
Module: domain.model.account.human.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from domain import Account
from software import Subscriber


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
    _subscriber: Subscriber
    
    def account(
            self,
            subscriber: Subscriber,
    ):
        """
        Args:
            subscriber: Subscriber
        """
        super().__init__(id=subscriber.id)
        self._subscriber = subscriber
        
    @property
    def subscriber(self) -> Subscriber:
        return self._subscriber
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, HumanAccount):
            return self.id == other.id
        return False
