# src/logic/coord/database/kernel/operation/exception.py

"""
Module: logic.coord.database.kernel.operation.pusher
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import RankService
from system import InsertionResult, LoggingLevelRouter
from logic.coord import (
    PushingDuplicateCoordException, RankQuotaAnalysis, RankQuotaFullException, Coord, CoordCollisionAnalysis,
    CoordStackFullException,
    CoordStackPushException, CoordStackService, CoordStackState
)


class CoordStackPush:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Coord insertion exception owner.
        2.  Guarantees all coords are safe and unique.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    coord: Coord,
                    coord_stack: CoordStackService,
            ) -> InsertionResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            coord: Coord,
            coord_stack: CoordStackService,
    ) -> InsertionResult[bool]:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    -   The coord is not safe.
                    -   One of its properties already in use.
                    -   The CoordStackService cannot support another coord.
            2.  If none of the failure conditions are met insert the coord and send the success result.
        Args:
           coord: Coord
           coord_stack: CoordStackService
        Returns:
            InsertionResult
        Raises:
            CoordStackPushException
        """
        method =  f"{cls.__name__}.push"
        
        # Handle the case that, the coord does not past a validation check.
        validation_result = coord_stack.run.build(coord)
        if validation_result.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=CoordStackPushException.OP,
                    msg=CoordStackPushException.MSG,
                    err_code=CoordStackPushException.ERR_CODE,
                    mthd_rslt_type=CoordStackPushException.MTHD_RSLT,
                    ex=validation_result.exception
                )
            )
        # Handle the case that, the coord is already on top of the schema.
        if coord == coord_stack.current_item:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    op=CoordStackPushException.OP,
                    msg=CoordStackPushException.MSG,
                    err_code=CoordStackPushException.ERR_CODE,
                    mthd_rslt_type=CoordStackPushException.MTHD_RSLT,
                    ex=PushingDuplicateCoordException(
                        msg=PushingDuplicateCoordException.MSG,
                        err_code=PushingDuplicateCoordException.ERR_CODE,
                    )
                )
            )
        # --- Push the coord onto the schema, then send the work product.---#
        coord_stack.items.append(coord)
        return InsertionResult.success()

    