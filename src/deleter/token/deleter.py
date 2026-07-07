# src/deleter/token/deleter.py

"""
Module: deleter.token.deleter
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from deleter import Deleter
from err import TokenDeleterException
from model import Token
from permitter.deletion import TokenDeletionPermitter
from report import DeletionApprovalReport
from result import DeletionResult, MethodResultType
from stack import TokenStackService, TokenStackState
from util import LoggingLevelRouter


class TokenDeleter(Deleter[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token deletion exception owner.
        2.  Prevent deleting from an empty stack.
        
    Attributes:
    
    Provides:
        -   execute(
                item_id: int,
                stack: TokenStackService,
                permitter: TokenDeletionPermitter,
        ) -> DeletionResult[Token]
        
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls, 
            item_id: int,
            stack: TokenStackService,
            permitter: TokenDeletionPermitter | None = None,
    ) -> DeletionResult[Token]:
        """
        Remove the token at the top of the stack.
        
        Action:
            1.  Send an exception chain in the DeletionResult if the stack is empty.
            2.  Otherwise, delete the token from the stack.
            3.  Send the success result containing the finished work product.
        Args:
            item_id: int
            stack: TokenStackService
            permitter: TokenDeletionPermitter
        Returns:
            DeletionResult[Token]
        Raises:
            TokenDeleterException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if permitter is None:
            permitter = TokenDeletionPermitter()
        
        permission_analysis_result = permitter.execute(item_id=item_id, stack=stack)
        # Handle the case that, the push_permitter does not complete analysis.
        if permission_analysis_result.is_failure:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenDeleterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDeleterException.MSG,
                    err_code=TokenDeleterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=permission_analysis_result.exception
                )
            )
        
        delete_permission = cast(DeletionApprovalReport, permission_analysis_result.payload)
        # Handle the case that, push permission is denied.
        if delete_permission.is_denied:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenDeleterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenDeleterException.MSG,
                    err_code=TokenDeleterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=delete_permission.exception
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for token in stack.items:
            if token.id == item_id:
                # Record a hit before pulling it from the stack.
                target = token
                stack.items.remove(token)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        if target is None:
            return DeletionResult.nothing_to_delete()
        if stack.is_empty:
            stack.stack_state = TokenStackState.DEPLOYED_ON_BOARD
        return DeletionResult.success(target)
