# src/logic/token/database/kernel/operation/handler.py

"""
Module: logic.token.database.kernel.operation.pusher
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations

from logic.rank import RankService
from logic.system import InsertionResult, LoggingLevelRouter
from logic.token import (
    RankQuotaAnalysis, RankQuotaFullException, Token, TokenCollisionDetectionProcess, TokenStackFullException,
    TokenStackPushException, TokenStackService, TokenStackState
)


class TokenStackPushPusher:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token insertion process owner.
        2.  Guarantees all tokens are safe and unique.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
                    collision_detector: TokenCollisionDetectionProcess = TokenCollisionDetectionProcess(),
            ) -> InsertionResult

    Super:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_stack: TokenStackService,
            rank_service: RankService = RankService(),
            rank_quota_analyzer: RankQuotaAnalysis = RankQuotaAnalysis(),
            collision_detector: TokenCollisionDetectionProcess = TokenCollisionDetectionProcess(),
    ) -> InsertionResult[bool]:
        """
        Action:
            1.  Return a failure result containing an exception chain if
                    *   The token is not safe.
                    *   One of its properties already in use.
                    *   The TokenStackService cannot support another token.
            2.  If none of the failure conditions are met insert the token and send the success result.
        Args:
           token: Token
           rank_service: RankService
           token_stack: TokenStackService
           rank_quota_analyzer: RankQuotaAnalysis
           collision_detector: TokenCollisionDetectionProcess
        Returns:
            InsertionResult
        Raises:
            TokenStackPushException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.push"
        
        # Handle the case that, the list is full.
        if token_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                    mthd=method,
                    op=TokenStackPushException.OP,
                    msg=TokenStackPushException.MSG,
                    err_code=TokenStackPushException.ERR_CODE,
                    rslt_type=TokenStackPushException.RSLT_TYPE,
                    ex=TokenStackFullException(
                        msg=TokenStackFullException.MSG,
                        err_code=TokenStackFullException.ERR_CODE,
                    )
                )
            )
        # Request a collision report. The token is verified during the report generation. ---#
        collision_detection_result = collision_detector.execute(
            target=token,
            dataset=token_stack.items,
        )
        # Handle the case that, the either a collision was detected or token wis not safe.
        if not collision_detection_result.is_no_collision:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        rslt_type=TokenStackPushException.RSLT_TYPE,
                        ex=collision_detection_result.exception
                )
            )
        # --- Request a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.execute(
            rank=token.rank,
            token_stack=token_stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                    op=TokenStackPushException.OP,
                    msg=TokenStackPushException.MSG,
                    mthd=TokenStackPushException.MTHD,
                    rslt_type=TokenStackPushException.RSLT_TYPE,
                    ex=rank_quota_report.exception
                )
            )
        # Handle the case that, there's no open slots for the token's rank.
        if rank_quota_report.payload.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                    op=TokenStackPushException.OP,
                    msg=TokenStackPushException.MSG,
                    mthd=TokenStackPushException.MTHD,
                    rslt_type=TokenStackPushException.RSLT_TYPE,
                    ex=RankQuotaFullException(
                        msg=RankQuotaFullException.MSG,
                        err_code=RankQuotaFullException.ERR_CODE,
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Push the token onto the stack
        token_stack.items.append(token)
        # Maintain state.
        if token_stack.is_full:
            token_stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    