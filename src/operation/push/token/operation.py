# src/operation/push/token/operation.py

"""
Module: operation.push.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from err import TokenPusherException
from model import Token
from operation import Pusher
from permitter import TokenPushPermitter
from report import PushApproval
from result import InsertionResult, MethodResultType
from stack import TokenStackService, TokenStackState
from util import LoggingLevelRouter


class TokenPusher(Pusher[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token insertion exception owner.
        2.  Guarantees all tokens are safe and unique.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    item: Token,
                    stack: TokenStackService,
                    push_permitter: TokenPushPermitter,
            ) -> InsertionResult

    Super Class:
        Pusher
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            item: Token,
            stack: TokenStackService,
            push_permitter: TokenPushPermitter | None = None,
    ) -> InsertionResult:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The token is not safe.
                    *   One of its properties already in use.
                    *   The TokenStackService cannot support another token.
            2.  If none of the failure conditions are met insert the token and send the success result.
        Args:
            item: Token
            stack: TokenStackService
            push_permitter: TokenPushPermitter
        Returns:
            InsertionResult
        Raises:
            TokenPusherException
        """
        method =  f"{cls.__name__}.push"
    
    
        if push_permitter is None:
            push_permitter = TokenPushPermitter()
            
        permission_analysis_result = push_permitter.execute(item=item, stack=stack)
        if permission_analysis_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=permission_analysis_result.exception
                )
            )
        permission = cast(PushApproval, permission_analysis_result.payload)
        if permission.is_denied:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=permission.exception
                )
            )
        # Push the token onto the stack
        stack.items.append(item)
        # Maintain state.
        if stack.is_full:
            stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    