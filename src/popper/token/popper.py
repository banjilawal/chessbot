# src/popper/token/operation.py

"""
Module: popper.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import TokenPopperException
from model import Token
from permitter import TokenPopPermitter
from popper import Popper
from request import PopRequest
from result import DeletionResult, MethodResultType
from stack import TokenStackState
from util import LoggingLevelRouter


class TokenPopper(Popper[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token deletion exception owner.
        2.  Prevent deleting from an empty stack.

    Attributes:
        permitter: TokenPopPermitter
        
    Provides:
        -   execute(stack: TokenStackService,) -> DeletionResult

    Super Class:
        Popper
    """
    _permitter: TokenPopPermitter | None = None
    
    def __init__(self, permitter: TokenPopPermitter | None = TokenPopPermitter()):
        """
        Args:
            permitter: TokenPopPermitter
        """
        self._permitter = permitter

    @LoggingLevelRouter.monitor
    def execute(self, request: PopRequest) -> DeletionResult:
        """
        Action:
            1.  Return an exception chain in the DeletionResult if permission is
                not granted for the pop.
            2.  Otherwise, remove the topmost token then, send the success result.
        Args:
            request: PopRequest
        Returns:
            DeletionResult
        Raises:
            TokenPopperException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, push rights are not granted.
        permission = self._permitter.run(request=request)
        if permission.is_denied:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenPopperException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPopperException.MSG,
                    err_code=TokenPopperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=permission.exception
                )
            )
        # Otherwise, complete the pop steps.
        target = request.stack.items.pop(-1)
        if request.stack.is_empty:
            request.stack.stack_state = TokenStackState.DEPLOYED_ON_BOARD
        return DeletionResult.success(target)
