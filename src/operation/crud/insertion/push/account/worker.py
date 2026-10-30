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
from collection import AccountStack
from domain import Account
from err import AccountPusherException
from exchange import AccountPushPermissionRequest, AccountPushRequest
from operation import Pusher
from transit import AccountPushPermissionDispatcher
from util import IdFactory, LoggingLevelRouter


class AccountPusher(Pusher[AccountPushRequest]):
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
        Pusher
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
            1.  Send an exception in the Response if the permitter sends a denial.
            2.  If the item already exists, send a success Response.
            3.  Otherwise, append to the collection before sending the success.
        Args:
            request: AccountPushRequest
        Result:
            InsertionResult
        Raises:
            AccountPusherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that the permission_dispatcher sends a denial.
        permission = self.permitter.execute(
            request=AccountPushPermissionRequest(
                authorization_applicant=request,
                id=IdFactory.next_id(class_name="AccountPushPermissionRequest"),
            )
        )
        if permission.request_is_denied:
            # Send a failure in the Response
            return InsertionResult.failure(
                AccountPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPusherException.MSG,
                    err_code=AccountPusherException.ERR_CODE,
                    ex=permission.exception,
                )
            )
        # If the 
        if permission.item_already_exists:
            return InsertionResult.already_inserted()
        
        approved_request = cast(AccountPushRequest, permission.approval)
        item = cast(Account, approved_request.item)
        collection = cast(AccountStack, approved_request.collection)
        collection.items.append(item)
        return InsertionResult.success()