# src/transit/dispatcher/authorization/computation/product/dispatcher.py

"""
Module: transit.dispatcher.authorization.computation.product.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ScalarProductDecision
from authorization import ScalarProductPermitter
from exchange import ScalarProductPermissionRequest, VectorProductRequest
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter


class ScalarProductPermissionDispatcher(
    ComputationPermissionDispatcher[ScalarProductPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a ScalarProductPermitter then send the results
            back to clients.

    Attributes:
        permitter: ScalarProductPermitter

    Provides:
        -   def  execute(candidate: Any) -> PushDecision

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[ScalarProductPermitter] | None = None):
        """
        Args:
             permitter: Optional[ScalarProductPermitter]
        """
        super().__init__(permitter=permitter or ScalarProductPermitter())
        
    @property
    def permitter(self) -> ScalarProductPermitter:
        return cast(ScalarProductPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ScalarProductDecision:
        """
        Make a decision about a VectorProductRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the VectorProductRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            ScalarProductDecision
        Raises:
            ScalarProductPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductPermissionDispatcherException.MSG,
                    err_code=ScalarProductPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for product processing. ---#
        permission_request = cast(ScalarProductPermissionRequest, decision.permission_request)
        transaction_request = cast(VectorProductRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return ScalarProductDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )