# src/artifact/decision/crud/insertion/add/vector/decision.py

"""
Module: artfifact.decision.crud.insertion.add.vector.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat import AddNodeDecision, Permission
from exchange import AddVectorNodePermissionRequest, AddVectorNodeRequest


class AddVectorNodeDecision(
    AddNodeDecision[AddVectorNodePermissionRequest, AddVectorNodeRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[AddRequest]

    Provides:

    Super Class:
        AddNodeDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            transaction_request: Optional[AddVectorNodeRequest] | None = None,
            permission_request: Optional[AddVectorNodePermissionRequest] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            transaction_request: Optional[AddVectorNodeRequest]
            permission_request: Optional[AddVectorNodePermissionRequest]
            exception: Optional[Exception]
        """
        super().__init__(
            transaction_request=transaction_request,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )