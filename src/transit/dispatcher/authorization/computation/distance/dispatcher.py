# src/transit/dispatcher/authorization/computation/distance/dispatcher.py

"""
Module: transit.dispatcher.authorization.computation.distance.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import DistanceComputationDecision
from authorization import DistanceComputationPermitter
from request import DistanceComputationPermissionRequest, DistanceRequest, EuclideanDistanceRequest
from transit import ComputationPermissionDispatcher
from util import LoggingLevelRouter


class DistanceComputationPermissionDispatcher(
    ComputationPermissionDispatcher[DistanceComputationPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Distribute jobs between DistanceComputationPermitters then send the results
            back to clients.

    Attributes:
        permitter: DistanceComputationPermitter

    Provides:
        -   def  execute(candidate: Any) -> PushDecision

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[DistanceComputationPermitter] | None = None):
        """
        Args:
             permitter: Optional[DistanceComputationPermitter]
        """
        super().__init__(permitter=permitter or DistanceComputationPermitter())
        
    @property
    def permitter(self) -> DistanceComputationPermitter:
        return cast(DistanceComputationPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DistanceComputationDecision:
        """
        Make a decision about a VectorDistanceRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the VectorDistanceRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            DistanceComputationDecision
        Raises:
            DistanceComputationPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        decision = self.permitter.execute(candidate)
        # Handle the case that the permitter does not grant permission.
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=DistanceComputationPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=DistanceComputationPermissionDispatcherException.MSG,
                    err_code=DistanceComputationPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for distance processing. ---#
        permission_request = cast(DistanceComputationPermissionRequest, decision.permission_request)
        transaction_request = cast(DistanceRequest, decision.transaction_request)

        # --- Prepare and forward the transaction approval. ---#
        return DistanceComputationDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )