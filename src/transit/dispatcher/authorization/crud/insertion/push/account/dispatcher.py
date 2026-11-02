# src/transit/dispatcher/authorization/crud/push/account/dispatcher.py

"""
Module: transit.dispatcher.authorization.crud.push.account.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional, cast

from artifcat import AccountPushDecision
from authorization import AccountPushPermitter
from err import AccountPushRequestNullException
from exchange import AccountPushPermissionRequest
from transit import PushPermissionDispatcher
from util import LoggingLevelRouter


class AccountPushPermissionDispatcher(
    PushPermissionDispatcher[AccountPushPermissionRequest]
):
    """
    Role
        -   Authorization Process Flow

    Responsibilities:
        1.  Direct jobs towards an AccountPushPermitter then send the results
            back to clients.

    Attributes:
        permitter: AccountPushPermitter

    Provides:
        -   def  execute(candidate: Any) -> PushDecision

    Super Class:
        PushPermissionDispatcher
    """
    
    def __init__(self, permitter: Optional[AccountPushPermitter] | None = None):
        """
        Args:
             permitter: Optional[AccountPushPermitter]
        """
        super().__init__(permitter=permitter or AccountPushPermitter())
        
    @property
    def permitter(self) -> AccountPushPermitter:
        return cast(AccountPushPermitter, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, candidate: Any) -> AccountPushDecision:
        """
        Make a decision about an AccountPushRequest.
        
        Action:
            1.  Send an exception chain in the denial if any of the
                following occur.
                    -   The permitter issues a denial.
                    -   Either the AccountPushRequest or its PermissionRequest
                        are null
            2.  Otherwise, send a grant decision.
        Args:
            candidate: Any
        Returns:
            AccountPushDecision
        Raises:
            AccountPushPermissionDispatcherException
        """
        method = f"{self.__class__.__name__}.execution"
        
        # Handle the case that the permitter does not grant permission.
        decision = self.permitter.execute(candidate)
        if decision.request_is_denied:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionDispatcherException.MSG,
                    err_code=AccountPushPermissionDispatcherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = decision.permission_request
        transaction_request = decision.transaction_request
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionDispatcherException.MSG,
                    err_code=AccountPushPermissionDispatcherException.ERR_CODE,
                    ex=AccountPushPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return AccountPushDecision.denial(
                exception=AccountPushPermissionDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushPermissionDispatcherException.MSG,
                    err_code=AccountPushPermissionDispatcherException.ERR_CODE,
                    ex=AccountPushRequestNullException()
                )
            )
        # --- Prepare and forward the transaction approval. ---#
        return AccountPushDecision.grant(
            transaction_request=transaction_request,
            permission_request=permission_request,
        )