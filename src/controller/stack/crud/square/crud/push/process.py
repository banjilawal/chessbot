# src/logic/square/database/kernel/operation/exception.py

"""
Module: logic.square.database.kernel.operation.pusher
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import RankService
from system import InsertionResult, LoggingLevelRouter
from logic.square import (
    SquareStackCapacityAnalyzer, SquareStackCapacityFullException, Square, SquareCollisionAnalysis, SquareStackFullException,
    SquareStackPushException, SquareStackService, SquareStackState
)


class SquareStackPush:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Square insertion exception owner.
        2.  Guarantees all squares are safe and unique.

    Attributes:

    Provides:
        -   push(
                    cls,
                    square: Square,
                    square_stack: SquareStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: SquareStackCapacityAnalysis = SquareStackCapacityAnalysis(),
                    collision_detector: SquareCollisionAnalyst = SquareCollisionAnalyst(),
            ) -> InsertionResult

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            square: Square,
            square_stack: SquareStackService,
            rank_service: RankService = RankService(),
            rank_quota_analyzer: SquareStackCapacityAnalyzer = SquareStackCapacityAnalyzer(),
            collision_detector: SquareCollisionAnalysis = SquareCollisionAnalysis(),
    ) -> InsertionResult[bool]:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The square is not safe.
                    *   One of its properties already in use.
                    *   The SquareStackService cannot support another square.
            2.  If none of the failure conditions are met insert the square and send the success result.
        Args:
           square: Square
           rank_service: RankService
           square_stack: SquareStackService
           rank_quota_analyzer: SquareStackCapacityAnalysis
           collision_detector: SquareCollisionAnalyst
        Returns:
            InsertionResult
        Raises:
            SquareStackPushException
            SquareStackFullException
        """
        method =  f"{cls.__name__}.push"
        
        # Handle the case that, the list is full.
        if square_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackPushException(
                    cls_mthd=method,
                    op=SquareStackPushException.OP,
                    msg=SquareStackPushException.MSG,
                    err_code=SquareStackPushException.ERR_CODE,
                    mthd_rslt_type=SquareStackPushException.MTHD_RSLT,
                    ex=SquareStackFullException(
                        msg=SquareStackFullException.MSG,
                        err_code=SquareStackFullException.ERR_CODE,
                    )
                )
            )
        # ServiceRequest a collision report. The square is verified during the report generation. ---#
        collision_detection_result = collision_detector.build(
            attractor=square,
            dataset=square_stack.items,
        )
        # Handle the case that, the either a collision was detected or square wis not safe.
        if not collision_detection_result.is_no_collisions:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackPushException(
                        op=SquareStackPushException.OP,
                        msg=SquareStackPushException.MSG,
                        mthd=SquareStackPushException.MTHD,
                        mthd_rslt_type=SquareStackPushException.MTHD_RSLT,
                        ex=collision_detection_result.exception
                )
            )
        # --- ServiceRequest a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.search_service(
            rank=square.rank,
            square_stack=square_stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackPushException(
                    op=SquareStackPushException.OP,
                    msg=SquareStackPushException.MSG,
                    mthd=SquareStackPushException.MTHD,
                    mthd_rslt_type=SquareStackPushException.MTHD_RSLT,
                    ex=rank_quota_report.exception
                )
            )
        # Handle the case that, there's no open slots for the square's rank.
        if rank_quota_report.payload.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                SquareStackPushException(
                    op=SquareStackPushException.OP,
                    msg=SquareStackPushException.MSG,
                    mthd=SquareStackPushException.MTHD,
                    mthd_rslt_type=SquareStackPushException.MTHD_RSLT,
                    ex=SquareStackCapacityFullException(
                        msg=SquareStackCapacityFullException.MSG,
                        err_code=SquareStackCapacityFullException.ERR_CODE,
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Push the square onto the schema
        square_stack.items.append(square)
        # Maintain state.
        if square_stack.is_full:
            square_stack.state = SquareStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    