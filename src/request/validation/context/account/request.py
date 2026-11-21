# src/request/validation/context/account/request.py

"""
Module: request.validation.context.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from domain import AccountContext
from request import ContextValidationRequest
from transit import AccountContextCarrier


class AccountContextValidationRequest(ContextValidationRequest[AccountContext]):
    """
     Role:
         -  Messaging

     Responsibilities:
         1. Provide details about an AccountContextValidation job.

     Attributes:
         id: int
         item: AccountContextCarrier

     Provides:
     
     Super Class:
        ContextValidationRequest
     """
    
    def __init__(self, id: int, item: AccountContextCarrier):
        """
        Args:
            id: int
            item: AccountContextCarrier
        """
        super().__init__(id=id, item=item)

    @property
    def item(self) -> AccountContextCarrier:
        return cast(AccountContextCarrier, super().item)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountContextValidationRequest):
            return self.id == other.id
        return False