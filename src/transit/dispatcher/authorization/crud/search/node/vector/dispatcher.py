# src/transit/dispatcher/authorization/crud/search/node/vector/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.search.node.vector.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import VectorNodeSearchDecision
from authorization import VectorNodeSearchPermitter
from err import VectorNodeSearchPermissionDispatcherException
from request import VectorNodeSearchPermissionRequest, VectorNodeSearchRequest
from transit import SearchPermissionDispatcher
from util import LoggingLevelRouter


class VectorNodeSearchPermissionDispatcher(
    SearchPermissionDispatcher[VectorNodeSearchPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards an VectorNodeSearchPermitters then send the results
            back to clients.

    Attributes:
        permitter: VectorNodeSearchPermitter

    Provides:
        -   def  execute(candidate: Any) -> SearchDecision

    Super Class:
        SearchPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[VectorNodeSearchPermitter] | None = None):
        """
        Args:
             permitter: Optional[VectorNodeSearchPermitter]
        """
        super().__init__(permitter=permitter or VectorNodeSearchPermitter())
        
    @property
    def permitter(self) -> VectorNodeSearchPermitter:
        return cast(VectorNodeSearchPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> VectorNodeSearchDecision:
        """
        Make a decision about an VectorNodeSearchRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the VectorNodeSearchRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            SearchDecision
        Raises:
            VectorNodeSearchPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return VectorNodeSearchDecision.denial(
                exception=VectorNodeSearchPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorNodeSearchPermissionDispatcherException.MSG,
                    err_code=VectorNodeSearchPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(VectorNodeSearchPermissionRequest, decision.permission_request)
        transaction_request = cast(VectorNodeSearchRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return VectorNodeSearchDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )