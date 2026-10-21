# src/operation/collection/insertion/stack.token/operation.py

"""
Module: operation.collection.insertion.stack.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import TokenStackPushAuthorizer, TokenStackPushRequest
from collection import TokenStackState
from err import TokenStackPushException
from domain.model import Token
from operation import StackPop
from artifcat import InsertionResult, MethodResultType
from util import LoggingLevelRouter


class TokenStackPush(StackPop[Token]):
    """
    Role
        - Worker

    Responsibilities:
        1.  Add an item to the TokenStackService

    Attributes:
        authorizer: TokenStackPushAuthorizer
        
    Provides:
        -   def execute(request: TokenStackPushAuthorizer) -> InsertionResult

    Super Class:
        StackPush
    """
    
    def __init__(self, authorizer: Optional[TokenStackPushAuthorizer] | None = None):
        """
        Args:
            authorizer: Optional[TokenStackPushAuthorizer]
        """
        super().__init__(authorizer=authorizer or TokenStackPushAuthorizer())
    
    @property
    def authorizer(self) -> TokenStackPushAuthorizer:
        return cast(TokenStackPushAuthorizer, super().authorizer)
    
    
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
        
        # Handle the case that push rights are not granted.
        decision = self._authorizer.execute(job=request)
        if decision.is_denied:
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
        req = cast(TokenStackPushRequest, decision.operation)
        # Otherwise, complete the push steps.
        req.stack.items.append(req.item)
        # Maintain state.
        if req.stack.has_both_slots_occupied:
            req.stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()