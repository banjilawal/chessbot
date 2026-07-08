# src/deleter/token/deleter.py

"""
Module: deleter.token.deleter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from deleter import Deleter
from err import TokenDeleterException
from model import Token
from permitter import TokenDeletionPermitter
from request import DeletionRequest
from result import DeletionResult, MethodResultType
from stack import TokenStackState
from util import LoggingLevelRouter


class TokenDeleter(Deleter[Token]):
    """
    Role:
        - CRUD Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token deletion exception owner.
        2.  Prevent deleting from an empty stack.

    Attributes:
        permitter: TokenDeletionPermitter
        
    Provides:
        -   execute(item_id: int, stack: TokenStackService,) -> DeletionResult

    Super Class:
        Deleter
    """
    _permitter: TokenDeletionPermitter | None = None
    
    def __init__(self, permitter: TokenDeletionPermitter | None = TokenDeletionPermitter()):
        """
        Args:
            permitter: TokenDeletionPermitter
        """
        self._permitter = permitter
    
    @LoggingLevelRouter.monitor
    def execute(self, request: DeletionRequest,) -> DeletionResult:
        """
        Action:
            1.  Return an exception chain in the DeletionResult if permission is
                not granted for the deletion.
            2.  Otherwise, remove the topmost token then, send the success result.
        Args:
            request: DeletionRequest
        Returns:
            DeletionResult
        Raises:
            TokenDeleterException
        """
        method = f"{self.__class__.__name__}.execute"
        
        # Handle the case that, push rights are not granted.
        permission = self._permitter.run(request=request)
        if permission.is_denied:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenDeleterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenDeleterException.MSG,
                    err_code=TokenDeleterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=permission.exception
                )
            )
        stack = request.stack
        # Otherwise, complete the deletion steps.
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for token in stack.items:
            if token.id == request.item_id:
                # Record a hit before pulling it from the stack.
                target = token
                stack.items.remove(token)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        if target is None:
            return DeletionResult.nothing_to_delete()
        if stack.is_empty:
            stack.stack_state = TokenStackState.DEPLOYED_ON_BOARD
        return DeletionResult.success(target)
