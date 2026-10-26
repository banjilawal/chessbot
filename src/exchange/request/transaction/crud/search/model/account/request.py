# src/exchange/request/transaction/crud/search/model/account/request.py

"""
Module: exchange.request.transaction.crud.search.model.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from collection import AccountStack
from domain import Account
from exchange import SearchRequest


class AccountSearchRequest(SearchRequest[Account]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide job details to an AccountSearcher

     Attributes:
         id: int
         item: Account
         collection: AccountStack

     Provides:

     Super Class:
        SearchRequest
     """
    
    def __init__(self, id: int, context: AccountContext, collection: AccountStack):
        """
        Args:
            id: int
            item: Account
            collection: AccountStack
        """
        super().__init__(id, context=context, collection=collection)
        
    @property
    def item(self) -> Account:
        return cast(Account, super().item)
    
    @property
    def collection(self) -> AccountStack:
        return cast(AccountStack, super().collection)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountSearchRequest):
            return self.id == other.id
        return False