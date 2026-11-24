# src/transit/dispatcher/authorization/crud/remove/vector/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.remove.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import RemoveVectorNodeDecision
from authorization import RemoveVectorNodePermitter

from err import RemoveVectorNodePermissionDispatcherException
from request import RemoveVectorNodePermissionRequest, RemoveVectorNodeRequest
from transit import RemoveNodePermissionDispatcher
from util import LoggingLevelRouter


class RemoveVectorNodePermissionDispatcher(
    RemoveNodePermissionDispatcher[RemoveVectorNodePermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards an RemoveVectorNodePermitters then send the results
            back to clients.

    Attributes:
        permitter: RemoveVectorNodePermitter

    Provides:
        -   def  execute(candidate: Any) -> RemoveDecision

    Super Class:
        RemoveNodePermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[RemoveVectorNodePermitter] | None = None):
        """
        Args:
             permitter: Optional[RemoveVectorNodePermitter]
        """
        super().__init__(permitter=permitter or RemoveVectorNodePermitter())
        
    @property
    def permitter(self) -> RemoveVectorNodePermitter:
        return cast(RemoveVectorNodePermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> RemoveVectorNodeDecision:
        """
        Make a decision about an RemoveVectorNodeRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the RemoveVectorNodeRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            RemoveVectorNodeDecision
        Raises:
            RemoveVectorNodePermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return RemoveVectorNodeDecision.denial(
                exception=RemoveVectorNodePermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=RemoveVectorNodePermissionDispatcherException.MSG,
                    err_code=RemoveVectorNodePermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for removeitional processing. ---#
        permission_request = cast(RemoveVectorNodePermissionRequest, decision.permission_request)
        transaction_request = cast(RemoveVectorNodeRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return RemoveVectorNodeDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )