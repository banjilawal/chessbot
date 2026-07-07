# src/pusher/token/pusher.py

"""
Module: pusher.token.pusher
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenPusherException
from model import Token
from permitter import TokenPushPermitter
from pusher import Pusher
from request import PushRequest
from result import InsertionResult, MethodResultType
from stack import TokenStackService, TokenStackState
from util import IdFactory, LoggingLevelRouter


class TokenPusher(Pusher[Token]):
    """
    Role:
        - Transaction pipeline
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token insertion process owner.

    Attributes:
        permitter: TokenPushPermitter
        
    Provides:
        -   execute(self, item: Token, stack: TokenStackService,) -> InsertionResult

    Super Class:
        Pusher
    """
    _permitter: TokenPushPermitter | None = None
    
    def __init__(self, permitter: TokenPushPermitter | None = TokenPushPermitter()):
        """
        Args:
            permitter: TokenPushPermitter
        """
        self._permitter = permitter
        
    
    @LoggingLevelRouter.monitor
    def execute(self, item: Token, stack: TokenStackService,) -> InsertionResult:
        """
        Action:
            1.  Return an exception chain in the InsertionResult if permission is
                not granted for the push.
            2.  Otherwise, perform the insertion then, send the success result.
        Args:
            item: Token
            stack: TokenStackService
        Returns:
            InsertionResult
        Raises:
            TokenPusherException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, push rights are not granted.
        permission = self._permitter.run(
            request=PushRequest(
                item=item,
                stack=stack,
                id=IdFactory.next_id(class_name="PushRequest"),
            )
        )
        if permission.is_denied:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=permission.exception
                )
            )
        # Otherwise, complete the push steps.
        stack.items.append(item)
        # Maintain state.
        if stack.is_full:
            stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    