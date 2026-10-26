# src/operation/crud/insertion/push/account/worker.py

"""
Module: operation.crud.insertion.push.account.worker
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionResponse, InsertionResult, ResponseState
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
    def execute(self, request: AccountPushRequest) -> InsertionResponse:
        """
        Args:
            request: AccountPushRequest
        Result:
            InsertionResult
        Raises:
            AccountPusherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        permission = self.permitter.execute(
            request=AccountPushPermissionRequest(
                candidate=request,
                id=IdFactory.next_id(class_name="AccountPushPermissionRequest"),
            )
        )
        if permission.request_is_denied:
            return InsertionResult.failure(
                AccountPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPusherException.MSG,
                    err_code=AccountPusherException.ERR_CODE,
                    ex=permission.exception,
                )
            )
        approved_request = cast(AccountPushRequest, permission.approval)
        null_response = InsertionResponse.success(
            request=approved_request,
            result=InsertionResult.already_inserted(),
        )
        if permission.item_already_exists:
            return null_response
        
        item = cast(Account, approved_request.item)
        collection = cast(AccountStack, approved_request.collection)
        collection.items.append(item)
        
        
        return InsertionResponse.success(
            request=approved_request,
            result=InsertionResult.success(),
        )