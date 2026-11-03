# src/artifact/decision/crud/search/model/account/decision.py

"""
Module: artfifact.decision.crud.search.model.account.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import ModelSearchDecision, Permission
from exchange import AccountSearchPermissionRequest, AccountSearchRequest


class AccountSearchDecision(
    ModelSearchDecision[AccountSearchPermissionRequest, AccountSearchRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an AccountSearch transaction is permitted.

    Attributes:
        transaction_request: Optional[AccountSearchRequest]
        permission_request: Optional[AccountSearchPermissionRequest]

    Provides:

    Super Class:
        ModelSearchDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[AccountSearchRequest] | None = None,
            permission_request: Optional[AccountSearchPermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[AccountSearchRequest]
            permission_request: Optional[AccountSearchPermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
    
    @property
    def transaction_request(self) -> Optional[AccountSearchRequest]:
        return cast(AccountSearchRequest, super().transaction_request)
    
    @property
    def permission_request(self) -> Optional[AccountSearchPermissionRequest]:
        return cast(AccountSearchPermissionRequest, super().permission_request)


    
