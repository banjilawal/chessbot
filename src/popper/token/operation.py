# src/popper/token/operation.py

"""
Module: popper.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from err import TokenPopperException
from model import Token
from operation import Popper
from permitter import TokenPopPermitter
from report import PopApproval
from result import DeletionResult, MethodResultType
from stack import TokenStackService, TokenStackState
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
    
    Provides:
        -   pop() -> DeletionResult[Token]
        -   delete_by_id(id: int, identity_service: IdentityService) -> DeletionResult[Token]
        
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            stack: TokenStackService,
            permitter: TokenPopPermitter | None = None,
    ) -> DeletionResult[Token]:
        """
        Remove the token at the top of the stack.
        
        Action:
            1.  Send an exception chain in the DeletionResult if the stack is empty.
            2.  Otherwise, pop the token from the stack.
            3.  Send the success result containing the finished work product.
        Args:
            item_id: int
            stack: TokenStackService
            permitter: TokenPopPermitter
        Returns:
            DeletionResult[Token]
        Raises:
            TokenPopperException
        """
        method = f"{cls.__class__.__name__}.execute"
        
        if permitter is None:
            permitter = TokenPopPermitter()
        
        permission_analysis_result = permitter.execute(stack=stack)
        # Handle the case that, the push_permitter does not complete analysis.
        if permission_analysis_result.is_failure:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenPopperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopperException.MSG,
                    err_code=TokenPopperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=permission_analysis_result.exception
                )
            )
        
        pop_permission = cast(PopApproval, permission_analysis_result.payload)
        # Handle the case that, push permission is denied.
        if pop_permission.is_denied:
            # Return the exception chain on failure
            return DeletionResult.failure(
                TokenPopperException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopperException.MSG,
                    err_code=TokenPopperException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.DELETION_RESULT,
                    ex=permission.exception
                )
            )
        target = stack.items.pop(-1)
        if stack.is_empty:
            stack.stack_state = TokenStackState.DEPLOYED_ON_BOARD
        return DeletionResult.success(target)
