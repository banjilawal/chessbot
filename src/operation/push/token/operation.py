# src/operation/push/token/operation.py

"""
Module: operation.push.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from analyzer import RankQuotaAnalyzer
from detector import TokenCollisionDetector
from microservice import RankService
from model import Token
from operation import Pusher
from result import InsertionResult
from stack import TokenStackService
from util import LoggingLevelRouter


class TokenPusher(Pusher[Token]):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Token insertion exception owner.
        2.  Guarantees all tokens are safe and unique.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
            ) -> InsertionResult

    Super Class:
    """
    
    @classmethod
    @LoggingLevelRouter.monitor
    def execute(
            cls,
            token: Token,
            token_stack: TokenStackService,
            rank_service: RankService | None = None,
            rank_quota_analyzer: RankQuotaAnalyzer | None = None,
            collision_detector: TokenCollisionDetector | None = None,
    ) -> InsertionResult:
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
           rank_quota_analyzer: RankQuotaAnalyzer
           collision_detector: TokenCollisionAnalyst
        Returns:
            InsertionResult
        Raises:
            TokenStackPushException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.push"
    
    
        if rank_service is None:
            rank_service = RankService()
        if rank_quota_analyzer is None:
            rank_quota_analyzer = RankQuotaAnalyzer()
        if collision_detector is None:
            collision_detector = TokenCollisionDetector()
        
        # Handle the case that, the list is full.
        if token_stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                    cls_mthd=method,
                    op=TokenStackPushException.OP,
                    msg=TokenStackPushException.MSG,
                    err_code=TokenStackPushException.ERR_CODE,
                    mthd_rslt_type=TokenStackPushException.MTHD_RSLT,
                    ex=TokenStackFullException(
                        msg=TokenStackFullException.MSG,
                        err_code=TokenStackFullException.ERR_CODE,
                    )
                )
            )
        # ServiceRequest a collision report. The token is verified during the report generation. ---#
        collision_detection_result = collision_detector.execute(
            target=token,
            dataset=token_stack.items,
        )
        # Handle the case that, the either a collision was detected or token wis not safe.
        if not collision_detection_result.is_no_collisions:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenStackPushException(
                        op=TokenStackPushException.OP,
                        msg=TokenStackPushException.MSG,
                        mthd=TokenStackPushException.MTHD,
                        mthd_rslt_type=TokenStackPushException.MTHD_RSLT,
                        ex=collision_detection_result.exception
                )
            )
        # --- ServiceRequest a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.execute(
            rank=token.rank,
            stream=token_stack,
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
                    mthd_rslt_type=TokenStackPushException.MTHD_RSLT,
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
                    mthd_rslt_type=TokenStackPushException.MTHD_RSLT,
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

    