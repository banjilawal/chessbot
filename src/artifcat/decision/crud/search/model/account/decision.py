# src/artifact/decision/crud/search/model/account/decision.py

"""
Module: artfifact.decision.crud.search.model.account.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import ModelSearchDecision, Permission
from exchange import AccountSearchPermissionRequest, AccountSearchRequest


class AccountSearchDecision(
    ModelSearchDecision[AccountSearchPermissionRequest, AccountSearchRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[SearchRequest]

    Provides:

    Super Class:
        ModelSearchDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[AccountSearchRequest] | None = None,
            permission_request: Optional[AccountSearchPermissionRequest] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            transaction_request: Optional[T]
            permission_request: Optional[P]
            exception: Optional[Exception]
        """
        super().__init__(
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )


    
