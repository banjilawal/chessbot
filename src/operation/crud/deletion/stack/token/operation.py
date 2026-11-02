# src/operation/crud/delete/stack.token/operator.py

"""
Module: operation.crud.delete.stack.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from authorization import TokenStackPopDispatcher, TokenStackPopRequest
from repo.collection import TokenStackState
from err import TokenStackPopException
from domain.model import Token
from operation import StackPop
from artifcat import DeletionResult, MethodResultType
from util import LoggingLevelRouter


class TokenStackPop(StackPop[Token]):
    """
    Role:
        -   Transaction Worker

    Responsibilities:
        1.  Add an item to the TokenStackService

    Attributes:
        dispatcher: TokenStackPopDispatcher
        
    Provides:
        -   def execute(request: TokenStackPopDispatcher) -> DeletionResult

    Super Class:
        StackPop
    """
    
    def __init__(self, dispatcher: Optional[TokenStackPopDispatcher] | None = None):
        """
        Args:
            dispatcher: Optional[TokenStackPopDispatcher]
        """
        super().__init__(dispatcher=dispatcher or TokenStackPopDispatcher())
    
    @property
    def dispatcher(self) -> TokenStackPopDispatcher:
        return cast(TokenStackPopDispatcher, super().dispatcher)
    
    
    @LoggingLevelRouter.monitor
    def execute(self, request: TokenStackPopRequest) -> DeletionResult:
        """
        Action:
            1.  Return an exception chain in the DeletionResult if permission is
                not granted for the pop.
            2.  Otherwise, perform the deletion then, send the success result.
        Args:
            request: TokenStackPopRequest
        Returns:
            DeletionResult
        Raises:
            TokenStackPoperException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that pop rights are not granted.
        decision = self._dispatcher.execute(job=request)
        if decision.request_is_denied:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenStackPopException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenStackPopException.MSG,
                    err_code=TokenStackPopException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETE_RESULT,
                    ex=decision.exception
                )
            )
        stack = cast(TokenStackPopRequest, decision.operation).stack
        item = cast(TokenStackPopRequest, decision.operation).item
        
        # Otherwise, complete the pop steps.
        product = stack.items.remove(item)
        # Maintain state.
        if stack.is_blank:
            stack.validation_state = TokenStackState.DEPLOYED_ON_BOARD
        
        # --- Send the work product ---#
        return DeletionResult.success(product)