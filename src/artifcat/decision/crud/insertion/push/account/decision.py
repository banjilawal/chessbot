# src/artifact/decision/crud/insertion/push/account/decision.py

"""
Module: artfifact.decision.crud.insertion.push.account.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import Permission, PushDecision
from artifcat.decision.decision import T
from exchange import AccountPushPermissionRequest, AccountPushRequest


class AccountPushDecision(
    PushDecision[AccountPushPermissionRequest, AccountPushRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an AccountPush transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        PushDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[AccountPushRequest] | None = None,
            permission_request: Optional[AccountPushPermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[AccountPushRequest]
            permission_request: Optional[AccountPushPermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
        
    @property
    def transaction_request(self) -> Optional[AccountPushRequest]:
        return cast(AccountPushRequest, super().transaction_request)
    
    @property
    def permission_request(self) -> Optional[AccountPushPermissionRequest]:
        return cast(AccountPushPermissionRequest, super().permission_request)