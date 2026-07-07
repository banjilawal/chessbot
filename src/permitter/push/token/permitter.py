# src/push/token/py

"""
Module: push.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Type, cast

from analyzer import RankQuotaAnalyzer
from bootstrapper import PrimingValidator
from detector import TokenCollisionDetector
from err import PushRequestNullException, TokenPushPermitterException, TokenStackNullException
from microservice import RankService
from model import Token
from permitter import PushPermitter
from report import PushApprovalReport
from request import PushRequest
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter
from validator import TokenValidator


class TokenPushPermitter(PushPermitter):
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a push.

    Attributes:
        token_validator: TokenValidator
        rank_service: RankService
        quota_analyzer: RankQuotaAnalyzer
        collision_detector: TokenCollisionDetector
        priming_validator: PrimingValidator

    Provides:
        -   execute(request: PushRequest) -> PushApprovalReport

    Super Class:
    """
    _token_validator: TokenValidator
    _rank_service: RankService
    _quota_analyzer: RankQuotaAnalyzer
    _collision_detector: TokenCollisionDetector
    _priming_validator: PrimingValidator
    
    def __init__(
            self,
            token_validator: TokenValidator | None = TokenValidator(),
            rank_service: RankService | None = RankService(),
            quota_analyzer: RankQuotaAnalyzer | None = RankQuotaAnalyzer(),
            collision_detector: TokenCollisionDetector | None = TokenCollisionDetector(),
            priming_validator: PrimingValidator | None = PrimingValidator(),
    ):
        """
        Args:
            rank_service: RankService
            quota_analyzer: RankQuotaAnalyzer
            collision_detector: TokenCollisionDetector
            priming_validator: PrimingValidator
        """
        self._token_validator = token_validator
        self._rank_service = rank_service
        self._quota_analyzer = quota_analyzer
        self._collision_detector = collision_detector
        self._priming_validator = priming_validator
        
        
    @LoggingLevelRouter.monitor
    def run(self, request: PushRequest, ) -> PushApprovalReport:
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
            request: PushRequest
        Returns:
            AnalysisResult
        Raises:
            TokenPushPermitterException
            TokenStackFullException
        """
        method =  f"{self.__class__.__name__}.execute"
        
        # Handle the case that, the request is malformed
        request_type_validation_result  = self._priming_validator.execute(
            candidate=request,
            target_model=Type[PushRequest],
            null_exception=PushRequestNullException()
        )
        # Send the exception chain in the permission denial.
        if request_type_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=request_type_validation_result.exception,
                )
            )
        token_validation_result = self._token_validator.execute(candidate=request.item)
        if token_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=request_type_validation_result.exception,
                )
            )
        stack_validation_result = self._priming_validator.execute(
            candidate=request.stack,
            target_model=Type[TokenStackService],
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=request_type_validation_result.exception,
                )
            )
        token = cast(Token, token_validation_result.payload)
        stack = cast(TokenStackService, stack_validation_result.payload)
        
        report = self._collision_detector.execute(attractor=token, stream=stack)
        if report.collision_exists:
            PushApprovalReport.deny(
                exception=TokenPushPermitterException(
                    cls_mthd=method,
                    cls_name=self.__class__.__name__,
                    msg=TokenPushPermitterException.MSG,
                    err_code=TokenPushPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=report.exception,
                )
            )
        quota_analysis_result = self._quota_analyzer.execute(
            rank=token.rank,
            token_stack=stack,
        )
        if quota_analysis_result.is_failure
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
                PushApprovalReport.deny(
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
                PushApprovalReport.deny(
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
                PushApprovalReport.deny(
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
        return AnalysisResult.completed(PushApprovalReport.approve(item=item, stack=stack))

    