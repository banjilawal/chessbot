# src/operation/push/token/operation.py

"""
Module: operation.push.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from http.cookiejar import request_port
from operator import itemgetter
from typing import cast

from analyzer import RankQuotaAnalyzer
from blueprint import TokenBlueprint
from detector import TokenCollisionDetector
from err import RankQuotaFullException, TokenPusherException
from microservice import RankService
from model import Token
from operation import Pusher, TokenStackFullException
from report import CollisionReport
from report.quota.report import RankQuotaReport
from result import InsertionResult, MethodResultType
from stack import TokenStackService, TokenStackState
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
            item: Token,
            stack: TokenStackService,
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
            TokenPusherException
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
        if stack.is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=TokenStackFullException(
                        msg=TokenStackFullException.MSG,
                        err_code=TokenStackFullException.ERR_CODE,
                    )
                )
            )
        # ServiceRequest a collision report. The token is verified during the report generation. ---#
        blueprint = TokenBlueprint(id=item.id, rank=item.rank, opening_square=item.opening_square, team=item.team, )
        collision_detection_result = collision_detector.execute(
            target=item,
            stack=stack,
        )
        if collision_detection_result.failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=collision_detection_result.exception,
                )
            )
        report = cast(CollisionReport, collision_detection_result.payload)
        # Handle the case that, the either a collision was detected or token wis not safe.
        if report.collision_exists:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=report.exception,
                )
            )
        # --- ServiceRequest a rank quota report. ---#
        rank_quota_report = rank_quota_analyzer.execute(
            rank=item.rank,
            stream=stack,
            rank_service=rank_service,
        )
        # Handle the case that, the request was not completed.
        if rank_quota_report.is_failure:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=rank_quota_report.exception,
                )
            )
        quota_report = cast(RankQuotaReport, rank_quota_report.payload)
        # Handle the case that, there's no open slots for the token's rank.
        if quota_report.rank_is_full:
            # Return the exception chain on failure
            return InsertionResult.failure(
                TokenPusherException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPusherException.MSG,
                    err_code=TokenPusherException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.INSERTION_RESULT,
                    ex=RankQuotaFullException(
                        msg=RankQuotaFullException.MSG,
                        err_code=RankQuotaFullException.ERR_CODE,
                    ),
                )
            )
        # --- Integrity and performance tests are passed. ---#
        
        # Push the token onto the stack
        stack.items.append(item)
        # Maintain state.
        if stack.is_full:
            stack.state = TokenStackState.READY_FOR_DEPLOYMENT
        
        # --- Send the work product ---#
        return InsertionResult.success()

    