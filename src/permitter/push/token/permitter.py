# src/push/token/py

"""
Module: push.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import cast

from analyzer import RankQuotaAnalyzer
from detector import TokenCollisionDetector
from err import RankQuotaFullException, TokenPushPermitterException, TokenStackFullException
from microservice import RankService
from model import Token
from report import CollisionReport, PushApproval, RankQuotaReport
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter


class TokenPushPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a push.

    Attributes:

    Provides:
        -   execute(
                    cls,
                    token: Token,
                    token_stack: TokenStackService,
                    rank_service: RankService = RankService(),
                    rank_quota_analyzer: RankQuotaAnalyzer = RankQuotaAnalyzer(),
                    collision_detector: TokenCollisionAnalyst = TokenCollisionAnalyst(),
            ) -> AnalysisResult

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
    ) -> AnalysisResult:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a push denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            item: Token
            stack: TokenStackService
            rank_service: RankService
            rank_quota_analyzer: RankQuotaAnalyzer
            collision_detector: TokenCollisionAnalyst
        Returns:
            AnalysisResult
        Raises:
            TokenPushPermitterException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.push"
    
        if rank_service is None:
            rank_service = RankService()
        if rank_quota_analyzer is None:
            rank_quota_analyzer = RankQuotaAnalyzer()
        if collision_detector is None:
            collision_detector = TokenCollisionDetector()
        
        # ServiceRequest a collision report. The token is verified during the report generation. ---#
        collision_detection_result = collision_detector.execute(
            attractor=item,
            stream=stack,
        )
        # Handle the case that, the collision_detection is not completed.
        if collision_detection_result.failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=collision_detection_result.exception,
                )
            )
        
        # --- ServiceRequest a rank quota report. ---#
        quota_analysis_result = rank_quota_analyzer.execute(
            rank=item.rank,
            stream=stack,
            rank_service=rank_service,
        )
        # Handle the case that, the quota analysis was not completed.
        if quota_analysis_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=quota_analysis_result.exception,
                )
            )
        
        # Handle the case that, the list is full.
        if stack.is_full:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                PushApproval.deny(
                    exception=TokenPushPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPushPermitterException.MSG,
                        err_code=TokenPushPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=TokenStackFullException(
                            msg=TokenStackFullException.MSG,
                            err_code=TokenStackFullException.ERR_CODE,
                        )
                    )
                )
            )
        

        report = cast(CollisionReport, collision_detection_result.payload)
        # Handle the case that, the either a collision was detected or token wis not safe.
        if report.collision_exists:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                PushApproval.deny(
                    exception=TokenPushPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPushPermitterException.MSG,
                        err_code=TokenPushPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=report.exception,
                    )
                )
            )

        quota = cast(RankQuotaReport, quota_analysis_result.payload)
        # Handle the case that, there's no open slots for the token's rank.
        if quota.rank_is_full:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                PushApproval.deny(
                    exception=TokenPushPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPushPermitterException.MSG,
                        err_code=TokenPushPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=RankQuotaFullException(
                            msg=RankQuotaFullException.MSG,
                            err_code=RankQuotaFullException.ERR_CODE,
                        ),
                    )
                )
            )

        # --- Integrity and performance tests are passed. ---#
        return AnalysisResult.completed(PushApproval.approve(item=item, stack=stack))

    