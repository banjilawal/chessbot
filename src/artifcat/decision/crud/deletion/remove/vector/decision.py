# src/artifact/decision/crud/deletion/remove/vector/decision.py

"""
Module: artfifact.decision.crud.deletion.remove.vector.decision
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from artifcat.decision.crud.deletion import RemoveNodeDecision
from exchange import RemoveVectorNodeRequest


class RemoveVectorNodeDecision(
    RemoveNodeDecision[RemoveVectorNodePermissionRequest, RemoveVectorNodeRequest]
):
    """
    Role:
        - Permission Reporting

    Responsibilities:
        1.  Report if a Crud transaction is permitted.

    Attributes:
        approval: Optional[RemoveRequest]

    Provides:

    Super Class:
        RemoveNodeDecision
    """
    
    def __init__(
            self,
            permission: Permission,
            approval: Optional[RemoveVectorNodeRequest] | None = None,
            permission_request: Optional[RemoveVectorNodePermissionRequest] | None = None,
            exception: Optional[Exception] | None = None,
    ):
        """
        Args:
            permission: Permission
            approval: Optional[RemoveVectorNodeRequest]
            permission_request: Optional[RemoveVectorNodePermissionRequest]
            exception: Optional[Exception]
        """
        super().__init__(
            approval=approval,
            exception=exception,
            permission=permission,
            permission_request=permission_request,
        )