# src/artifact/decision/crud/search/node/vector/decision.py

"""
Module: artfifact.decision.crud.search.node.vector.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import NodeSearchDecision, Permission
from request import VectorNodeSearchPermissionRequest, VectorNodeSearchRequest


class VectorNodeSearchDecision(
    NodeSearchDecision[VectorNodeSearchPermissionRequest, VectorNodeSearchRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an VectorNodeSearch transaction is permitted.

    Attributes:
        transaction_request: Optional[VectorNodeSearchRequest]
        permission_request: Optional[VectorNodeSearchPermissionRequest]

    Provides:

    Super Class:
        NodeSearchDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[VectorNodeSearchRequest] | None = None,
            permission_request: Optional[VectorNodeSearchPermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[VectorNodeSearchRequest]
            permission_request: Optional[VectorNodeSearchPermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
    
    @property
    def transaction_request(self) -> Optional[VectorNodeSearchRequest]:
        return cast(VectorNodeSearchRequest, super().transaction_request)
    
    @property
    def permission_request(self) -> Optional[VectorNodeSearchPermissionRequest]:
        return cast(VectorNodeSearchPermissionRequest, super().permission_request)


    
