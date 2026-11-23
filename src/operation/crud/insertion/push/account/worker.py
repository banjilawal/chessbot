# src/operation/crud/insertion/push/account/worker.py

"""
Module: operation.crud.insertion.push.account.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionResult
from operation import ModelPusher
from request import AccountPushPermissionRequest, AccountPushRequest
from transit import AccountPushPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class AccountPusher(ModelPusher[AccountPushRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an AccountPushRequest

    Attributes:
        permitter: AccountPushPermissionDispatcher

    Provides:
        -   def execute(request: AccountPushRequest) -> InsertionResult

    Super Class:
        ModelPusher
    """
    
    def __init__(
            self,
            permitter: Optional[AccountPushPermissionDispatcher] | None = None,
    ):
        """
        Args:
            permitter: Optional[AccountPushPermissionDispatcher]
        """
        super().__init__(permitter=permitter or AccountPushPermissionDispatcher())
    
    @property
    def permitter(self) -> AccountPushPermissionDispatcher:
        return cast(AccountPushPermissionDispatcher, super().permitter)
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushRequest) -> InsertionResult:
        """
        Add a new, unique account to the collection.
        
        Action:
            1.  Send an exception in the InsertionResult if any of the following occur.
                    -   The request is denied.
                    -   An approval lacks either the AccountPushRequest or its
                        PermissionRequest.
            2.  Otherwise, append to the collection before sending the success.
        Args:
            request: AccountPushRequest
        Result:
            InsertionResult
        Raises:
            AccountPusherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the permission_permitter sends a denial.
        decision = self.permitter.execute(
            candidate=AccountPushPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="AccountPushPermissionRequest"),
            )
        )
        if decision.request_is_denied:
            # Send a failure in the Result
            return InsertionResult.failure(
                AccountPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPusherException.MSG,
                    err_code=AccountPusherException.ERR_CODE,
                    ex=decision.exception,
                )
            )
        # --- Extract the requests for additional processing. ---#
        permission_request = cast(AccountPushPermissionRequest, decision.permission_request)
        transaction_request = cast(AccountPushRequest, decision.transaction_request)
        
        # Handle the case that the permission_request is null.
        if permission_request is None:
            # Send the exception chain in the denial.
            return InsertionResult.failure(
                exception=AcountPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AcountPusherException.MSG,
                    err_code=AcountPusherException.ERR_CODE,
                    ex=AccountPushPermissionRequestNullException(),
                )
            )
        # Handle the case that the transaction_request is null.
        if transaction_request is None:
            # Send the exception chain in the denial.
            return InsertionResult.failure(
                exception=AcountPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AcountPusherException.MSG,
                    err_code=AcountPusherException.ERR_CODE,
                    ex=AccountPushRequestNullException()
                )
            )
        # --- Extract the transaction participants. ---#
        item = transaction_request.item
        collection = transaction_request.collection
        
        # --- Perform transaction and state management work. ---#
        collection.items.append(item)
        # --- Forward the work product to the client. ---#
        return InsertionResult.success()