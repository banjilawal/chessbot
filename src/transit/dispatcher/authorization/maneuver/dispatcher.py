# src/transit/dispatcher/authorization/maneuver/dispatcher.py

"""
Module: transit.dispatcher.authorization.maneuver.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import ManeuverDecision
from authorization import ManeuverPermitter
from err import ManeuverPermissionDispatcherException
from exchange import ManeuverPermissionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter


class ManeuverPermissionDispatcher(
    PermissionDispatcher[ManeuverPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a ManeuverPermitter then send the results
            back to clients.

    Attributes:
        permitter: ManeuverPermitter

    Provides:
        -   def  execute(candidate: Any) -> ManeuverDecision

    Super Class:
        PermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[ManeuverPermitter] | None = None):
        """
        Args:
             permitter: Optional[ManeuverPermitter]
        """
        super().__init__(permitter=permitter or ManeuverPermitter())
        
    @property
    def permitter(self) -> ManeuverPermitter:
        return cast(ManeuverPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> ManeuverDecision:
        """
        Make a decision about a ManeuverRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the ManeuverRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            ManeuverDecision
        Raises:
            ManeuverPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermissionDispatcherException.MSG,
                    err_code=ManeuverPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermissionDispatcherException.MSG,
                    err_code=ManeuverPermissionDispatcherException.ERR_CODE,
                    ex=ManeuverPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return ManeuverDecision.denial(
                exception=ManeuverPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ManeuverPermissionDispatcherException.MSG,
                    err_code=ManeuverPermissionDispatcherException.ERR_CODE,
                    ex=ManeuverRequestNullException()
                )
            )
        # --- Prepare and forward the transaction approval. ---#
        return ManeuverDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )