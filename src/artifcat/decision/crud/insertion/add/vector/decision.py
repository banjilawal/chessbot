# src/artifact/decision/crud/insertion/add/vector/decision.py

"""
Module: artfifact.decision.crud.insertion.add.vector.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import AddNodeDecision, Permission
from exchange import AddVectorNodePermissionRequest, AddVectorNodeRequest


class AddVectorNodeDecision(
    AddNodeDecision[AddVectorNodePermissionRequest, AddVectorNodeRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if an AddVectorNode transaction is permitted.

    Attributes:

    Provides:

    Super Class:
        AddNodeDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            exception: Optional[Exception] | None = None,
            transaction_request: Optional[AddVectorNodeRequest] | None = None,
            permission_request: Optional[AddVectorNodePermissionRequest] | None = None,
    ):
        """
        Args:
            permission: Permission
            exception: Optional[Exception]
            transaction_request: Optional[AddVectorNodeRequest]
            permission_request: Optional[AddVectorNodePermissionRequest]
        """
        super().__init__(
            exception=exception,
            permission=permission,
            permission_request=permission_request,
            transaction_request=transaction_request,
        )
    
    @property
    def transaction_request(self) -> Optional[AddVectorNodeRequest]:
        return cast(AddVectorNodeRequest, super().transaction_request)
    
    @property
    def permission_request(self) -> Optional[AddVectorNodePermissionRequest]:
        return cast(AddVectorNodePermissionRequest, super().permission_request)
        
    