# src/operation/collection/insertion/stack.token/operation.py

"""
Module: operation.collection.insertion.stack.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import TokenStackPushPermitter, TokenStackPushRequest
from collection import TokenStackState
from err import TokenStackPushException
from model import Token
from operation import StackPop
from result import InsertionResult, MethodResultType
from util import LoggingLevelRouter


class TokenStackPush(StackPop[Token]):
    """
    Role
        -   Worker

    Responsibilities:
        1.  Add an item to the TokenStackService

    Attributes:
        permitter: TokenStackPushPermitter
        
    Provides:
        -   def execute(request: TokenStackPushPermitter) -> InsertionResult

    Super Class:
        StackPush
    """
    
    def __init__(self, permitter: Optional[TokenStackPushPermitter] | None = None):
        """
        Args:
            permitter: Optional[TokenStackPushPermitter]
        """
        super().__init__(permitter=permitter or TokenStackPushPermitter())
    
    @property
    def permitter(self) -> TokenStackPushPermitter:
        return cast(TokenStackPushPermitter, super().permitter)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenStackPushRequest) -> InsertionResult:
        """
        Action:
            1.  Return an exception chain in the InsertionResult if permission is
                not granted for the push.
            2.  Otherwise, perform the insertion then, send the success result.
        Args:
            request: TokenStackPushRequest
        Returns:
            InsertionResult
        Raises:
            TokenPusherException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, push rights are not granted.
        decision = self._permitter.execute(request=request)
        if decision.request_is_denied:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackPushException.MSG,
                    err_code=TokenStackPushException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=decision.exception
                )
            )
        req = cast(TokenStackPushRequest, decision.request)
        # Otherwise, complete the push steps.
        req.stack.items.append(req.item)
        # Maintain state.
        if req.stack.is_full:
            req.stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()