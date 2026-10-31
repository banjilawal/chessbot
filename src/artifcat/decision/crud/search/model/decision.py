# src/artifact/decision/crud/search/model/decision.py

"""
Module: artfifact.decision.crud.search.model.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from artifcat import CrudDecision, Permission, SearchDecision
from exchange import (
    PermissionRequest, CrudPermissionRequest, SearchPermissionRequest, SearchRequest
)

T = TypeVar("T", bound="SearchRequest")

class ModelSearchDecision(SearchDecision[T], ABC, Generic[T]):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[SearchRequest]

    Provides:
        -   def grant(
                    approval: SearchRequest,
                    permission_request: PermissionRequest,
            ) -> SearchDecision

        -   def denial(
                    permission_request: PermissionRequest,
                    exception: Exception,
            ) -> SearchDecision

    Super Class:
        CrudDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            permission_request: PermissionRequest[T],
            exception: Optional[Exception] | None = None,
            approval: Optional[T] | None = None,
    ):
        """
        Args:
            permission: Permission
            permission_request: PermissionRequest
            exception: Optional[Exception]
            approval: Optional[T]
        """
        super().__init__(
            permission_request=permission_request,
            approval=approval,
            exception=exception,
            permission=permission,
        )
    
    @classmethod
    def grant(
            cls, 
            approval: SearchRequest,
            permission_request: PermissionRequest,
    ) -> CrudDecision:
        role_request = cast(
            SearchPermissionRequest,
            permission_request,
        )
        return cls(
            approval=approval,
            permission_request=role_request,
            permission=Permission.GRANTED,
        )
    
    @classmethod
    def denial(
            cls, 
            permission_request: PermissionRequest,
            exception: Exception,
    ) -> CrudDecision:
        role_request = cast(
            CrudPermissionRequest,
            permission_request,
        )
        return cls(
            exception=exception,
            permission_request=role_request,
            permission=Permission.DENIED,
        )


    
