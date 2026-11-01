# src/artifact/decision/crud/search/model/decision.py

"""
Module: artfifact.decision.crud.search.model.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from artifcat import Permission, SearchDecision
from exchange import ModelSearchRequest, SearchPermissionRequest


P = TypeVar("P", bound="SearchPermissionRequest")
T = TypeVar("T", bound="ModelSearchRequest")

class ModelSearchDecision(SearchDecision[P, T], ABC, Generic[P, T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a ModelSearch transaction is permitted.

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
