# src/transit/dispatcher/authorization/crud/add/vector/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.add.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AddVectorNodeDecision
from authorization import AddVectorNodePermitter
from err import AddVectorNodePermissionDispatcherException
from request import AddVectorNodePermissionRequest, AddVectorNodeRequest
from transit import AddNodePermissionDispatcher
from util import LoggingLevelRouter


class AddVectorNodePermissionDispatcher(
    AddNodePermissionDispatcher[AddVectorNodePermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards an AddVectorNodePermitters then send the results
            back to clients.

    Attributes:
        permitter: AddVectorNodePermitter

    Provides:
        -   def  execute(candidate: Any) -> AddDecision

    Super Class:
        AddNodePermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[AddVectorNodePermitter] | None = None):
        """
        Args:
             permitter: Optional[AddVectorNodePermitter]
        """
        super().__init__(permitter=permitter or AddVectorNodePermitter())
        
    @property
    def permitter(self) -> AddVectorNodePermitter:
        return cast(AddVectorNodePermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AddVectorNodeDecision:
        """
        Make a decision about an AddVectorNodeRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the AddVectorNodeRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            AddVectorNodeDecision
        Raises:
            AddVectorNodePermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AddVectorNodeDecision.denial(
                exception=AddVectorNodePermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AddVectorNodePermissionDispatcherException.MSG,
                    err_code=AddVectorNodePermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(AddVectorNodePermissionRequest, decision.permission_request)
        transaction_request = cast(AddVectorNodeRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return AddVectorNodeDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )