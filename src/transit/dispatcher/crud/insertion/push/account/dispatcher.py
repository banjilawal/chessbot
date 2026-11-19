# src/transit/dispatcher/crud/insertion/push/account/dispatcher.py

"""
Module: transit.dispatcher.crud.insertion.push.account.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionResult
from err import ChessException
from exchange import AccountPushRequest
from operation import AccountPusher
from transit import PushDispatcher
from util import LoggingLevelRouter


class AccountPushDispatcher(PushDispatcher[AccountPushRequest, InsertionResult]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Direct jobs towards a worker then forward the results to clients.

    Attributes:
        worker: AccountPusher
        
    Provides:

    Super Class:
        PushDispatcher
    """
    
    def __init__(self, worker: Optional[AccountPusher] | None = None):
        """
        Args:
            worker: Optional[AccountPusher]
        """
        super().__init__(worker=worker or AccountPusher())
        
    @property
    def worker(self) -> AccountPusher:
        return cast(AccountPusher, super().worker)
        

    @LoggingLevelRouter.monitor
    def execute(self, request: AccountPushRequest) -> InsertionResult:
        result = self.worker.execute(request)
        if result.is_failure:
            return InsertionResult.failure(
                ChessException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=ChessException.MSG,
                    err_code=ChessException.ERR_CODE,
                    ex=result.exception
                )
            )
        return InsertionResult.success()
