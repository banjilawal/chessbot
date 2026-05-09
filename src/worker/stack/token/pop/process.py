# src/logic/token/database/kernel/operation/crud/pop/validator.py

"""
Module: logic.token.database.kernel.operation.crud.pop.popper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from system import DeletionResult, IdentityService, LoggingLevelRouter
from model.token import (
    PoppingEmptyTokenStackException, Token, TokenStackPopException, TokenStackService, TokenStackState
)

class TokenStackPop:
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
    def execute(cls, token_stack: TokenStackService) -> DeletionResult[Token]:
        """
        Remove the token at the top of the stack.
        
        Action:
            1.  Send an exception chain in the DeletionResult if the stack is empty.
            2.  Otherwise, pop the token from the stack.
            3.  Send the success result containing the finished work product.
        Args:
            token_stack: TokenStackService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackPopException
            PoppingEmptyTokenStackException
        """
        method = f"{cls.__class__.__name__}.pop"
        
        # Handle the case that the stack is empty.
        if token_stack.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenStackPopException(
                    cls_mthd=method,
                    op=TokenStackPopException.OP,
                    msg=TokenStackPopException.MSG,
                    err_code=TokenStackPopException.ERR_CODE,
                    mthd_rslt_type=TokenStackPopException.MTHD_RSLT,
                    ex=PoppingEmptyTokenStackException(
                        msg=PoppingEmptyTokenStackException.MSG,
                        err_code=PoppingEmptyTokenStackException.ERR_CODE,
                    )
                )
            )
        # Handoff delivery responsibility to the stack_state_processor.
        return cls._token_stack_state_processor(
            deleted_token=token_stack.items.pop(-1),
            token_stack=token_stack,
        )

    
    @classmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            cls,
            id: int,
            token_stack: TokenStackService,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Token]:
        """
        Action:
        Delete any tokens whose id matches the target.
        
        Actions:
            1.  Send an exception chain in the DeletionResult if the idis not safe
            2.  Otherwise, create a temp variable.
            3.  Iterate through the items. If any match the id store then in the temp variable
                before deleting.
            4.  Possible success conditions are:
                    *   Nothing to delete.
                    *   Return the deleted item.
        Args:
            id: int
            token_stack: TokenStackService
            identity_service: IdentityService
        Returns:
            DeletionResult[Token]
        Raises:
            TokenStackPopException
            PoppingEmptyTokenStackException
        """
        method = f"{cls.__name__}.delete_by_id"
        
        # Handle the case that the stack is empty.
        if token_stack.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenStackPopException(
                    cls_mthd=method,
                    op=TokenStackPopException.OP,
                    msg=TokenStackPopException.MSG,
                    err_code=TokenStackPopException.ERR_CODE,
                    mthd_rslt_type=TokenStackPopException.MTHD_RSLT,
                    ex=PoppingEmptyTokenStackException(
                        msg=PoppingEmptyTokenStackException.MSG,
                        err_code=PoppingEmptyTokenStackException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the idis not safe.
        id_validation_result = identity_service.validate_id(candidate=id)
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                TokenStackPopException(
                    cls_mthd=method,
                    op=TokenStackPopException.OP,
                    msg=TokenStackPopException.MSG,
                    err_code=TokenStackPopException.ERR_CODE,
                    mthd_rslt_type=TokenStackPopException.MTHD_RSLT,
                    ex=id_validation_result.exception
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for token in token_stack.items:
            if token.id == id:
                # Record a hit before pulling it from the stack.
                target = token
                token_stack.items.remove(token)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # Nothing was deleted
        if target is None:
            return DeletionResult.nothing_to_delete()
        
        # If an item was deleted, handoff delivery responsibility to the stack_state_processor.
        return cls._token_stack_state_processor(
            deleted_token=target,
            token_stack=token_stack,
        )
    
    @classmethod
    @LoggingLevelRouter.monitor
    def _token_stack_state_processor(
            cls,
            deleted_token: Token,
            token_stack: TokenStackService
    ) -> DeletionResult[Token]:
        """
        Action:
            1.  If the token_stack is empty token_stack.state = TokenStackState.DEPLOYED_ON_BOARD
        Args:
            deleted_token: Token
            token_stack: TokenStackService
        Returns:
            DeletionResult[Token]
        Raises:
            None
        """
        method = f"{cls.__name__}._token_stack_state_processor"
        
        if token_stack.is_empty:
            token_stack.state = TokenStackState.DEPLOYED_ON_BOARD
        # --- Send the work product. ---#
        return DeletionResult.success(payload=deleted_token)
