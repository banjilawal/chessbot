# src/logic/coord/database/kernel/operation/crud/pop/validator.py

"""
Module: logic.coord.database.kernel.operation.crud.pop.transaction
Author: Banji Lawal
Created: 2026-03-28
version: 1.0.0
"""

from __future__ import annotations

from logic.system import DeletionResult, IdentityService, LoggingLevelRouter
from logic.coord import (
    PoppingEmptyCoordStackException, Coord, CoordStackPopException, CoordStackService, CoordStackState
)

class CoordStackPop:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Coord deletion exception owner.
        2.  Prevent deleting from an empty schema.
        
    Attributes:
    
    Provides:
        -   execute(coord_stack: CoordStackService) -> DeletionResult[Coord]
        
    Super:
    """

    @classmethod
    @LoggingLevelRouter.monitor
    def execute(cls, coord_stack: CoordStackService) -> DeletionResult[Coord]:
        """
        Remove the coord at the top of the schema.
        
        Action:
            1.  Send an exception chain in the DeletionResult if the schema is empty.
            2.  Otherwise, pop the coord from the schema.
            3.  Send the success result containing the finished work product.
        Args:
            coord_stack: CoordStackService
        Returns:
            DeletionResult[Coord]
        Raises:
            CoordStackPopException
            PoppingEmptyCoordStackException
        """
        method = f"{cls.__class__.__name__}.pop"
        
        # Handle the case that the schema is empty.
        if coord_stack.is_empty:
            # Return the exception chain on failure.
            return DeletionResult.failure(
                CoordStackPopException(
                    mthd=method,
                    op=CoordStackPopException.OP,
                    msg=CoordStackPopException.MSG,
                    err_code=CoordStackPopException.ERR_CODE,
                    rslt_type=CoordStackPopException.RSLT_TYPE,
                    ex=PoppingEmptyCoordStackException(
                        msg=PoppingEmptyCoordStackException.MSG,
                        err_code=PoppingEmptyCoordStackException.ERR_CODE,
                    )
                )
            )
        # --- Send the work product. ---#
        return DeletionResult.success(coord_stack.items.pop(-1))