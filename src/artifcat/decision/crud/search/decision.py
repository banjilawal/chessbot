# src/artifact/decision/crud/search/decision.py

"""
Module: artfifact.decision.crud.search.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudDecision, Permission
from exchange import SearchPermissionRequest, SearchRequest

P = TypeVar("P", bound="SearchPermissionRequest")
T = TypeVar("T", bound="SearchRequest")


class SearchDecision(CrudDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Search transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        CrudDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            permission_request: Optional[P] | None = None,
            transaction_request: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            permission_request: Optional[P]
            transaction_request: Optional[T]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )