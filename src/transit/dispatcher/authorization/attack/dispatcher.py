# src/transit/dispatcher/authorization/attack/dispatcher.py

"""
Module: transit.dispatcher.authorization.attack.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AttackDecision
from authorization import AttackPermitter
from err import AttackPermissionDispatcherException
from exchange import AttackPermissionRequest
from transit import PermissionDispatcher
from util import LoggingLevelRouter


class AttackPermissionDispatcher(
    PermissionDispatcher[AttackPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards a AttackPermitter then send the results
            back to clients.

    Attributes:
        permitter: AttackPermitter

    Provides:
        -   def  execute(candidate: Any) -> AttackDecision

    Super Class:
        PermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[AttackPermitter] | None = None):
        """
        Args:
             permitter: Optional[AttackPermitter]
        """
        super().__init__(permitter=permitter or AttackPermitter())
        
    @property
    def permitter(self) -> AttackPermitter:
        return cast(AttackPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AttackDecision:
        """
        Make a decision about a AttackRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the AttackRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            AttackDecision
        Raises:
            AttackPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                exception=AttackPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackPermissionDispatcherException.MSG,
                    err_code=AttackPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                exception=AttackPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackPermissionDispatcherException.MSG,
                    err_code=AttackPermissionDispatcherException.ERR_CODE,
                    ex=AttackPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return AttackDecision.denial(
                exception=AttackPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AttackPermissionDispatcherException.MSG,
                    err_code=AttackPermissionDispatcherException.ERR_CODE,
                    ex=AttackRequestNullException()
                )
            )
        # --- Prepare and forward the transaction approval. ---#
        return AttackDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )