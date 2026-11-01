# src/exchange/request/permission/crud/deletion/pop/account/request.py

"""
Module: exchange.request.permission.crud.deletion.pop.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AccountPopRequest, PopPermissionRequest


class AccountPopPermissionRequest(
    PopPermissionRequest[AccountPopRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides an AccountPopPermitter with job details.

     Attributes:
         id: int
         authorization_applicant: : AccountPopRequest

     Provides:

     Super Class:
        PopPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: AccountPopRequest):
        """
        Args:
            id: int
            authorization_applicant: AccountPopRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
        
    @property
    def authorization_applicant(self) -> AccountPopRequest:
        return cast(AccountPopRequest, super().authorization_applicant)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountPopPermissionRequest):
            return self.id == other.id
        return False