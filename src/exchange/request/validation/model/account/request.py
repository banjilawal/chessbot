# src/exchange/request/validation/model/account/request.py

"""
Module: exchange.request.validation.model.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import ModelValidationRequest
from domain import Account
from transit import AccountCarrier


class AccountValidationRequest(ModelValidationRequest[Account]):
    """
     Role:
         -  Messaging

     Responsibilities:
        1. Provide details about a Account a validation job.

     Attributes:
         id: int
         item: AccountCarrier

     Provides:
     
     Super Class:
        ModelValidationRequest
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
        if isinstance(other, AccountValidationRequest):
            return self.id == other.id
        return False