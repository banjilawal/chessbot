# src/logic/coord/database/kernel/operation/exception.py

"""
Module: logic.coord.database.kernel.operation.pusher
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import RankService
from logic.system import InsertionResult, LoggingLevelRouter
from logic.coord import (
    RankQuotaAnalysis, RankQuotaFullException, Coord, CoordCollisionAnalysis, CoordStackFullException,
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
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
                    collision_detector: CoordCollisionAnalysis = CoordCollisionAnalysis(),
            ) -> InsertionResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            coord: Coord,
            coord_stack: CoordStackService,
            rank_service: RankService = RankService(),
            rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
            collision_detector: CoordCollisionAnalysis = CoordCollisionAnalysis(),
    ) -> InsertionResult[bool]:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The coord is not safe.
                    *   One of its properties already in use.
                    *   The CoordStackService cannot support another coord.
            2.  If none of the failure conditions are met insert the coord and send the success result.
        Args:
           coord: Coord
           rank_service: RankService
           coord_stack: CoordStackService
           rank_quota_analyzer: RankQuotaAnalysis
           collision_detector: CoordCollisionAnalysis
        Returns:
            InsertionResult
        Raises:
            CoordStackPushException
            CoordStackFullException
        """
        method =  f"{cls.__name__}.push"
        
        # Handle the case that, the list is full.
        if coord_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                    mthd=method,
                    op=CoordStackPushException.OP,
                    msg=CoordStackPushException.MSG,
                    err_code=CoordStackPushException.ERR_CODE,
                    rslt_type=CoordStackPushException.RSLT_TYPE,
                    ex=CoordStackFullException(
                        msg=CoordStackFullException.MSG,
                        err_code=CoordStackFullException.ERR_CODE,
                    )
                )
            )
        # Request a collision report. The coord is verified during the report generation. ---#
        collision_detection_result = collision_detector.execute(
            target=coord,
            dataset=coord_stack.items,
        )
        # Handle the case that, the either a collision was detected or coord wis not safe.
        if not collision_detection_result.is_no_collision:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                        op=CoordStackPushException.OP,
                        msg=CoordStackPushException.MSG,
                        mthd=CoordStackPushException.MTHD,
                        rslt_type=CoordStackPushException.RSLT_TYPE,
                        ex=collision_detection_result.exception
                )
            )
        # --- Request a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.execute(
            rank=coord.rank,
            coord_stack=coord_stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                    op=CoordStackPushException.OP,
                    msg=CoordStackPushException.MSG,
                    mthd=CoordStackPushException.MTHD,
                    rslt_type=CoordStackPushException.RSLT_TYPE,
                    ex=rank_quota_report.exception
                )
            )
        # Handle the case that, there's no open slots for the coord's rank.
        if rank_quota_report.payload.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                CoordStackPushException(
                    op=CoordStackPushException.OP,
                    msg=CoordStackPushException.MSG,
                    mthd=CoordStackPushException.MTHD,
                    rslt_type=CoordStackPushException.RSLT_TYPE,
                    ex=RankQuotaFullException(
                        msg=RankQuotaFullException.MSG,
                        err_code=RankQuotaFullException.ERR_CODE,
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Push the coord onto the stack
        coord_stack.items.append(coord)
        # Maintain state.
        if coord_stack.is_full:
            coord_stack.state = CoordStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    