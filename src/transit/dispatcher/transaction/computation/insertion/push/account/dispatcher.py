# src/transit/dispatcher/computation/insertion/push/account/dispatcher.py

"""
Module: transit.dispatcher.computation.insertion.push.account.dispatcher
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from artifcat import InsertionResult
from err import AccountPushDispatcherException
from exchange import AccountPushRequest
from operation import AccountPusher
from transit import PushDispatcher
from util import LoggingLevelRouter


class AccountPushDispatcher(PushDispatcher[AccountPushRequest, InsertionResult]):
    """
    Role
        -   Process Flow

    Responsibilities:
        1.  Distribute jobs between worker then forward the results to clients.

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
        """
        Search an AccountStack for context matches.

        Action:
            1.  Send an exception chain in the SearchResult if any of the following
                occur.
                    -   The request is denied.
                    -   An approved request lacks either the AccountSearchRequest or
                        its PermissionRequest.
            2.  If the search result is empy send a SearchResult.empty otherwise, send
                the success result.
        Args:
            request: AccountSearchRequest
        Result:
            SearchResult[List[Account]]
        Raises:
            AccountSearcherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # --- Handoff the request to a worker. ---#
        result = self.worker.execute(request)
        
        # Handle the case that the request is not fulfilled.
        if result.is_failure:
            # Send the exception chain in the result.
            return InsertionResult.failure(
                AccountPushDispatcherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=AccountPushDispatcherException.MSG,
                    err_code=AccountPushDispatcherException.ERR_CODE,
                    ex=result.exception
                )
            )
        # --- Forward the work product to the caller. ---#
        return InsertionResult.success()
