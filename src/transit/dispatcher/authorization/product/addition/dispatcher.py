# src/transit/dispatcher/authorization/computation/addition/dispatcher.py

"""
Module: transit.dispatcher.authorization.computation.addition.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import VectorAdditionDecision
from authorization import VectorAdditionPermitter
from exchange import VectorAdditionPermissionRequest, VectorAdditionRequest
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter


class VectorAdditionPermissionDispatcher(
    ComputationPermissionDispatcher[VectorAdditionPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a VectorAdditionPermitter then send the results
            back to clients.

    Attributes:
        permitter: VectorAdditionPermitter

    Provides:
        -   def  execute(candidate: Any) -> PushDecision

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[VectorAdditionPermitter] | None = None):
        """
        Args:
             permitter: Optional[VectorAdditionPermitter]
        """
        super().__init__(permitter=permitter or VectorAdditionPermitter())
        
    @property
    def permitter(self) -> VectorAdditionPermitter:
        return cast(VectorAdditionPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> VectorAdditionDecision:
        """
        Make a decision about a VectorAdditionRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the VectorAdditionRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            VectorAdditionDecision
        Raises:
            VectorAdditionPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return VectorAdditionDecision.denial(
                exception=VectorAdditionPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionPermissionDispatcherException.MSG,
                    err_code=VectorAdditionPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(VectorAdditionPermissionRequest, decision.permission_request)
        transaction_request = cast(VectorAdditionRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return VectorAdditionDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )