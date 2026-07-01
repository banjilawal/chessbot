# src/pop/token/py

"""
Module: pop.token.operation
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from err import PoppingEmptyTokenStackException, TokenPopPermitterException, TokenStackNullException
from microservice import IdentityService
from report import PopApproval
from result import AnalysisResult, MethodResultType
from stack import TokenStackService
from util import LoggingLevelRouter
from validation import ValidationPrimer


class TokenPopPermitter:
    """
    Role:
        - Transaction Worker
        - Consistency, Integrity Maintenance
        - Process Runner

    Responsibilities:
        1.  Run tests to see if permission can be granted to a TokenStackService to execute a pop.

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
            id: int,
            stack: TokenStackService,
            identity_service: IdentityService | None = None,
            validation_primer: ValidationPrimer | None = None,
    ) -> AnalysisResult:
        """
        Action:
            1.  Return a failure result containing an exception chain if either:
                    -   The collision_detector
                    -   The rank_quota_analyzer
                do not complete their work.
            2.  Otherwise, send a pop denial if
                    -   The TokenStack is full.
                    -   The item collides with an existing stack member.
                    -   The quota for the token's rank is full.
            3.  Send an approval if all the tests are passed.
        Args:
            id: int
            stack: TokenStackService
            identity_service: IdentityService
            validation_primer: ValidationPrimer
        Returns:
            AnalysisResult
        Raises:
            TokenPopPermitterException
            TokenStackFullException
        """
        method =  f"{cls.__name__}.execute"
    
        if identity_service is None:
            identity_service = IdentityService()
        if validation_primer is None:
            validation_primer = ValidationPrimer()
            
        id_validation_result = identity_service.validate_id(candidate=id)
        if id_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=id_validation_result.exception,
                )
            )
        
        stack_validation_result = validation_primer.validate(
            candidate=stack,
            target_model=TokenStackService,
            null_exception=TokenStackNullException()
        )
        if stack_validation_result.is_failure:
            # Return the exception chain on failure
            return AnalysisResult.failure(
                TokenPopPermitterException(
                    cls_mthd=method,
                    cls_name=cls.__name__,
                    msg=TokenPopPermitterException.MSG,
                    err_code=TokenPopPermitterException.ERR_CODE,
                    mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                    ex=stack_validation_result.exception,
                )
            )
        if stack.is_empty:
            # Return the exception chain on failure
            return AnalysisResult.completed(
                PopApproval.deny(
                    exception=TokenPopPermitterException(
                        cls_mthd=method,
                        cls_name=cls.__name__,
                        msg=TokenPopPermitterException.MSG,
                        err_code=TokenPopPermitterException.ERR_CODE,
                        mthd_rslt_type=MethodResultType.ANALYSIS_RESULT,
                        ex=PoppingEmptyTokenStackException(
                            cls_mthd=method,
                            cls_name=cls.__name__,
                            msg=PoppingEmptyTokenStackException.MSG,
                            err_code=PoppingEmptyTokenStackException.ERR_CODE,
                        ),
                    )
                )
            )
        # --- Integrity and performance tests are passed. ---#
        return AnalysisResult.completed(PopApproval.approve(id=id, stack=stack))

    