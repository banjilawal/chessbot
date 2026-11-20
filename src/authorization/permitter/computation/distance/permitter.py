# src/authorization/permitter/computation/distance/permitter.py

"""
Module: authorization.permitter.computation.distance.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import DistanceComputationDecision
from authorization import ComputationPermitter
from bootstrap import DistanceComputationAuthorizationLoader
from exchange import DistanceComputationPermissionRequest, VectorDistanceRequest
from util import LoggingLevelRouter


class DistanceComputationPermitter(ComputationPermitter[DistanceComputationPermissionRequest]):
    """
    Role:
        -   Permission Authorization

    Responsibilities:
        1.  Issue a scalarDecision about a ScalarPermissionRequest then forward
            that scalarDecision to a ScalarWorker.

    Attributes:
        loader: ComputationAuthorizationLoader[T]

    Provides:
        -   def execute(candidate: Any) -> ScalarDecision

    Super Class:
        ComputationPermitter
    """
    
    def __init__(self, loader: DistanceComputationAuthorizationLoader):
        """
        Args:
            loader: DistanceComputationAuthorizationLoader
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> DistanceComputationAuthorizationLoader:
        return cast(DistanceComputationAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> DistanceComputationDecision:
        """
        Checks if a DistanceComputationPermissionRequest can be granted.

        Action:
            1.  Send an exception in the denial if the loader cannot bootstrap
                the process.
            2.  Otherwise, send a DistanceComputation approval.
        Args:
            candidate: Any
        Returns:
           DistanceComputationDecision
        Raises:
            VectorDistancePermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return DistanceComputationDecision.denial(
                exception=VectorDistancePermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorDistancePermitterException.MSG,
                    err_code=VectorDistancePermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_request = cast(DistanceComputationPermissionRequest, bootstrap.permission_request)
        transaction_request = cast(VectorDistanceRequest, bootstrap.transaction_request)

        # --- Forward the approval. ---#
        return DistanceComputationDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        