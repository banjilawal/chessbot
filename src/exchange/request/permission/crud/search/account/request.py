# src/exchange/request/permission/crud/search/account/request.py

"""
Module: exchange.request.permission.crud.search.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AccountSearchRequest, SearchPermissionRequest

class AccountSearchPermissionRequest(
    SearchPermissionRequest[AccountSearchRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides an AccountSearchAuthorizer with a job.

     Attributes:
         id: int
         authorization_applicant: : AccountSearchRequest

     Provides:

     Super Class:
        SearchPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: AccountSearchRequest):
        """
        Args:
            id: int
            authorization_applicant: AccountSearchRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
    
    @property
    def authorization_applicant(self) -> AccountSearchRequest:
        return cast(AccountSearchRequest, super().authorization_applicant)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountSearchPermissionRequest):
            return self.id == other.id
        return False