# src/artifact/decision/crud/trim/chain/decision.py

"""
Module: artfifact.decision.crud.trim.chain.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from artifcat import TrimDecision
from request import ChainTrimPermissionRequest, ChainTrimRequest

P = TypeVar("P", bound="ChainTrimPermissionRequest")
T = TypeVar("T", bound="ChainTrimRequest")


class ChainTrimDecision(TrimDecision[P, T], Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        transaction_request: Optional[ChainRequest]

    Provides:

    Super Class:
        TrimDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[T] | None = None,
            permission_request: Optional[P] | None = None,
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