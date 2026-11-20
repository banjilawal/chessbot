# src/authorization/permitter/computation/product/permitter.py

"""
Module: authorization.permitter.computation.product.permitter
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, cast

from artifcat import ScalarProductDecision
from authorization import ComputationPermitter
from bootstrap import ScalarProductAuthorizationLoader
from exchange import ScalarProductPermissionRequest, ScalarProductRequest
from util import LoggingLevelRouter


class ScalarProductPermitter(ComputationPermitter[ScalarProductPermissionRequest]):
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
    
    def __init__(self, loader: ScalarProductAuthorizationLoader):
        """
        Args:
            loader: ScalarProductAuthorizationLoader
        """
        super().__init__(loader=loader)
    
    @property
    def loader(self) -> ScalarProductAuthorizationLoader:
        return cast(ScalarProductAuthorizationLoader, super().loader)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ScalarProductDecision:
        """
        Checks if a ScalarProductPermissionRequest can be granted.

        Action:
            1.  Send an exception in the denial if the loader cannot bootstrap
                the process.
            2.  Otherwise, send a ScalarProduct approval.
        Args:
            candidate: Any
        Returns:
           ScalarProductDecision
        Raises:
            ScalarProductPermitterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that loader does not bootstrap the process.
        bootstrap = self.loader.execute(candidate=candidate)
        if bootstrap.request_is_denied:
            # Send the exception chain in the denial.
            return ScalarProductDecision.denial(
                exception=ScalarProductPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ScalarProductPermitterException.MSG,
                    err_code=ScalarProductPermitterException.ERR_CODE,
                    ex=bootstrap.exception,
                )
            )
        # --- Extract the transaction_request for processing. ---#
        permission_request = cast(ScalarProductPermissionRequest, bootstrap.permission_request)
        transaction_request = cast(ScalarProductRequest, bootstrap.transaction_request)

        # --- Forward the approval. ---#
        return ScalarProductDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )
        