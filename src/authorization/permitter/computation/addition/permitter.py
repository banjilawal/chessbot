# src/authorization/permitter/computation/addition/permitter.py

"""
Module: authorization.permitter.computation.addition.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import VectorAdditionDecision
from authorization import ComputationPermitter
from bootstrap import VectorAdditionAuthorizationLoader
from request import VectorAdditionPermissionRequest, VectorAdditionRequest
from util import LoggingLevelRouter


class VectorAdditionPermitter(ComputationPermitter[VectorAdditionPermissionRequest]):
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
    
    def __init__(self, loader: Optional[VectorAdditionAuthorizationLoader] | None = None):
        """
        Args:
            loader: Optional[VectorAdditionAuthorizationLoader]
        """
        super().__init__(loader=loader or VectorAdditionAuthorizationLoader())
    
    @property
    def loader(self) -> VectorAdditionAuthorizationLoader:
        return cast(VectorAdditionAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> VectorAdditionDecision:
        """
        Checks if a VectorAdditionPermissionRequest can be granted.

        Action:
            1.  Send an exception in the denial if the loader cannot bootstrap
                the process.
            2.  Otherwise, send a VectorAddition approval.
        Args:
            candidate: Any
        Returns:
           VectorAdditionDecision
        Raises:
            VectorAdditionPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return VectorAdditionDecision.denial(
                exception=VectorAdditionPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=VectorAdditionPermitterException.MSG,
                    err_code=VectorAdditionPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_request = cast(VectorAdditionPermissionRequest, bootstrap.permission_request)
        transaction_request = cast(VectorAdditionRequest, bootstrap.transaction_request)

        # --- Forward the approval. ---#
        return VectorAdditionDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        