# src/exchange/request/permission/crud/insertion/push/model/account/request.py

"""
Module: exchange.request.permission.crud.insertion.push.model.account.request
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import cast

from exchange import AccountPushRequest, ModelPushPermissionRequest


class AccountPushPermissionRequest(
    ModelPushPermissionRequest[AccountPushRequest]
):
    """
     Role:
         -  Messaging

     Responsibilities:
        1.  Provides an AccountPushAuthorizer with job details.

     Attributes:
         id: int
         authorization_applicant: : AccountPushRequest

     Provides:

     Super Class:
        ModelPushPermissionRequest
     """
    
    def __init__(self, id: int, authorization_applicant: AccountPushRequest):
        """
        Args:
            id: int
            authorization_applicant: AccountPushRequest
        """
        super().__init__(id, authorization_applicant=authorization_applicant)
        
    @property
    def authorization_applicant(self) -> AccountPushRequest:
        return cast(AccountPushRequest, super().authorization_applicant)
        
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AccountPushPermissionRequest):
            return self.id == other.id
        return False