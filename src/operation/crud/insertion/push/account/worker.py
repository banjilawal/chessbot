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
from err import AccountPusherException
from exchange import AccountPushPermissionRequest, AccountPushRequest
from operation import Pusher
from transit import AccountPushPermissionPermitter
from util import IdFactory, LoggingLevelRouter


class AccountPusher(Pusher[AccountPushRequest]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Executes an AccountPushRequest

    Attributes:
        permitter: AccountPushPermissionPermitter

    Provides:
        -   def execute(request: AccountPushRequest) -> InsertionResult

    Super Class:
        Pusher
    """
    
    def __init__(
            self,
            permitter: Optional[AccountPushPermissionPermitter] | None = None,
    ):
        """
        Args:
            permitter: Optional[AccountPushPermissionPermitter]
        """
        super().__init__(permitter=permitter or AccountPushPermissionPermitter())
    
    
    @property
    def permitter(self) -> AccountPushPermissionPermitter:
        return cast(AccountPushPermissionPermitter, super().permitter)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushRequest) -> InsertionResult:
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
            permission_request=AccountPushPermissionRequest(
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
        push_request = cast(AccountPushRequest, permission.permission_request)