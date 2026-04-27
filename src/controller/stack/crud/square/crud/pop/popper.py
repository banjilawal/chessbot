# src/logic/square/database/kernel/operation/crud/pop/validator.py

"""
Module: logic.square.database.kernel.operation.crud.pop.popper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations

from system import DeletionResult, IdentityService, LoggingLevelRouter
from logic.square import (
    PoppingEmptySquareStackException, Square, SquareStackPopException, SquareStackService
)

class SquareStackPopper:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square deletion exception owner.
        2.  Prevent deleting from an empty schema.
        
    Attributes:
    
    Provides:
        -   pop() -> DeletionResult[Square]
        -   delete_by_id(id: int, identity_service: IdentityService) -> DeletionResult[Square]
        
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def pop(cls, square_stack: SquareStackService) -> DeletionResult[Square]:
        """
        Remove the square at the top of the schema.
        
        Action:
            1.  Send an exception chain in the DeletionResult if the schema is empty.
            2.  Otherwise, pop the square from the schema.
            3.  Send the success result containing the finished work product.
        Args:
            square_stack: SquareStackService
        Returns:
            DeletionResult[Square]
        Raises:
            SquareStackPopException
            PoppingEmptySquareStackException
        """
        method = f"{cls.__class__.__name__}.pop"
        
        # Handle the case that the schema is empty.
        if square_stack.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                SquareStackPopException(
                    cls_mthd=method,
                    op=SquareStackPopException.OP,
                    msg=SquareStackPopException.MSG,
                    err_code=SquareStackPopException.ERR_CODE,
                    mthd_rslt=SquareStackPopException.MTHD_RSLT,
                    ex=PoppingEmptySquareStackException(
                        msg=PoppingEmptySquareStackException.MSG,
                        err_code=PoppingEmptySquareStackException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return DeletionResult.success(square_stack.items.pop(-1))
    
    @classmethod
    @LoggingLevelRouter.monitor
    def delete_by_id(
            cls,
            id: int,
            square_stack: SquareStackService,
            identity_service: IdentityService = IdentityService()
    ) -> DeletionResult[Square]:
        """
        Action:
        Delete any squares whose id matches the target.
        
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
            square_stack: SquareStackService
            identity_service: IdentityService
        Returns:
            DeletionResult[Square]
        Raises:
            SquareStackPopException
            PoppingEmptySquareStackException
        """
        method = f"{cls.__name__}.delete_by_id"
        
        # Handle the case that the schema is empty.
        if square_stack.is_empty:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                SquareStackPopException(
                    cls_mthd=method,
                    op=SquareStackPopException.OP,
                    msg=SquareStackPopException.MSG,
                    err_code=SquareStackPopException.ERR_CODE,
                    mthd_rslt=SquareStackPopException.MTHD_RSLT,
                    ex=PoppingEmptySquareStackException(
                        msg=PoppingEmptySquareStackException.MSG,
                        err_code=PoppingEmptySquareStackException.ERR_CODE,
                    )
                )
            )
        # Handle the case that, the idis not safe.
        id_validation_result = identity_service.validate_id(candidate=id)
        if id_validation_result.is_failure:
            # Send the exception chain on failure.
            return DeletionResult.failure(
                SquareStackPopException(
                    cls_mthd=method,
                    op=SquareStackPopException.OP,
                    msg=SquareStackPopException.MSG,
                    err_code=SquareStackPopException.ERR_CODE,
                    mthd_rslt=SquareStackPopException.MTHD_RSLT,
                    ex=id_validation_result.exception
                )
            )
        # --- Loop through the collection to ensure all matches are removed. ---#
        target = None
        for square in square_stack.items:
            if square.id == id:
                # Record a hit before pulling it from the schema.
                target = square
                square_stack.items.remove(square)
        # --- After the purging loop finishes handle the possible return cases. ---#
        
        # Nothing was deleted
        if target is None:
            return DeletionResult.nothing_to_delete()
        
        # --- Send the work product. ---#
        return DeletionResult.success(target)
