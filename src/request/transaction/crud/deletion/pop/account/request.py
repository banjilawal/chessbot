# src/request/transaction/crud/deletion/pop/account/request.py

"""
Module: request.transaction.crud.deletion.pop.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import AccountStack
from domain import Account, AccountContext
from request import PopRequest

class AccountPopRequest(PopRequest[Account]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to an AccountPopper

     Attributes:
         id: int
         context: AccountContext
         collection: AccountStack

     Provides:

     Super Class:
        PopRequest
     """
    
    def __init__(self, id: int, context: AccountContext, collection: AccountStack):
        """
        Args:
            id: int
            context: AccountContext
            collection: AccountStack
        """
        super().__init__(id=id, context=context, collection=collection)
        
    @property
    def context(self) -> AccountContext:
        return cast(AccountContext, super().context)
    
    @property
    def collection(self) -> AccountStack:
        return cast(AccountStack, super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountPopRequest):
            return self.id == other.id
        return False