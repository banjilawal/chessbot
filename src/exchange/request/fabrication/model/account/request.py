# src/exchange/request/fabrication/model/account/request.py

"""
Module: exchange.request.fabrication.model.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelBuildRequest
from domain import Account
from transit import AccountCarrier


class AccountBuildRequest(ModelBuildRequest[Account]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Account a build job.

     Attributes:
         id: int
         item: AccountCarrier

     Provides:
     
     Super Class:
        ModelBuildRequest
     """
    
    def __init__(self, id: int, item: AccountCarrier):
        """
        Args:
            id: int
            item: AccountCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> AccountCarrier:
        return cast(AccountCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountBuildRequest):
            return self.id == other.id
        return False